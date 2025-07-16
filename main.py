from menu import show_menu, get_item_by_number
from cart import add_to_cart, show_cart, save_order, cart as current_cart, clear_cart, generate_check
from user import register_user, login_user, save_order_for_user, add_favorite, show_favorites
import json

print("Привіт! Це сервіс замовлення їжі :)")

auth_choice = input("1 — Зареєструватися, 2 — Увійти: ")

if auth_choice == "1":
    username = register_user()
elif auth_choice == "2":
    username = login_user()
else:
    print("Невірний вибір. Вихід.")
    exit()

def show_user_orders(name):
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)

    orders = users.get(name, {}).get("orders", [])
    if not orders:
        print("У тебе ще немає замовлень.")
        return

    print(f"Замовлення користувача {name}:")
    for i, order in enumerate(orders, 1):
        print(f"\nЗамовлення {i} (Статус: {order.get('status', 'Очікує')}):")
        for item, price in order["items"]:
            print(f"- {item}: {price} грн")
        print(f"Разом: {order['total']} грн")

while True:
    print("\n📋 Меню дій:")
    print("1 — Зробити нове замовлення")
    print("2 — Переглянути мої замовлення")
    print("3 — Додати страву в улюблене")
    print("4 — Показати улюблені страви")
    print("5 — Оновити статус останнього замовлення")
    print("0 — Вийти")

    action = input("Введи номер дії: ")

    if action == "1":
        show_menu()
        while True:
            choice = input("Введи номер страви (або '0' для завершення): ")
            if choice == "0":
                break
            if not choice.isdigit():
                print("Невірний вибір. Спробуй ще раз.")
                continue
            number = int(choice)
            item = get_item_by_number(number)
            if item is None:
                print("Такого номера немає в меню.")
                continue
            add_to_cart(item)
            print(f"✅ Додано до кошика: {item[0]}")
        total = show_cart()
        save_order(total)
        save_order_for_user(username, current_cart.copy(), total)
        generate_check(username, current_cart.copy(), total)
        clear_cart()
        print("✔ Замовлення збережено!")

    elif action == "2":
        show_user_orders(username)

    elif action == "3":
        number = int(input("Введи номер страви з меню, яку хочеш додати в улюблені: "))
        item = get_item_by_number(number)
        if item:
            add_favorite(username, item)
            print("✅ Додано в улюблені")

    elif action == "4":
        show_favorites(username)

    elif action == "5":
        with open("users.json", "r+", encoding="utf-8") as f:
            users = json.load(f)
            orders = users[username]["orders"]
            if not orders:
                print("Немає замовлень.")
            else:
                orders[-1]["status"] = "Доставлено"
                f.seek(0)
                json.dump(users, f, ensure_ascii=False, indent=2)
                f.truncate()
                print("📦 Статус останнього замовлення оновлено на 'Доставлено'.")

    elif action == "0":
        print("До побачення!")
        break

    else:
        print("Невірний вибір.")
