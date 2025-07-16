cart = []

def add_to_cart(item):
    cart.append(item)

def show_cart():
    print("\n🛒 Твоє замовлення:")
    total = 0
    for item, price in cart:
        print(f"- {item}: {price} грн")
        total += price
    print(f"Загальна сума: {total} грн")
    return total

def save_order(total):
    with open("order_history.txt", "a", encoding="utf-8") as f:
        f.write("Замовлення:\n")
        for item, price in cart:
            f.write(f"- {item}: {price} грн\n")
        f.write(f"Загальна сума: {total} грн\n")
        f.write("-" * 30 + "\n")

def generate_check(username, items, total):
    with open(f"check_{username}.txt", "w", encoding="utf-8") as f:
        f.write(f"Чек для {username}\n")
        f.write("Ваше замовлення:\n")
        for item, price in items:
            f.write(f"- {item}: {price} грн\n")
        f.write(f"Разом: {total} грн\n")
        f.write("Дякуємо за замовлення!\n")

def clear_cart():
    cart.clear()
