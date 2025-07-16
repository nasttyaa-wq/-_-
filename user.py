from data import load_users, save_users

users = load_users()

def register_user():
    name = input("Введи своє ім'я для реєстрації: ")
    if name in users:
        print("Ім'я вже зареєстровано.")
        return name
    address = input("Введи свою адресу: ")
    phone = input("Введи номер телефону: ")
    users[name] = {
        "orders": [],
        "favorites": [],
        "address": address,
        "phone": phone
    }
    save_users(users)
    print(f"Реєстрація успішна. Привіт, {name}!")
    return name

def login_user():
    name = input("Введи своє ім'я для входу: ")
    if name in users:
        print(f"Вхід виконано. Вітаємо назад, {name}!")
        return name
    print("Користувача не знайдено. Зареєструйся.")
    return register_user()

def save_order_for_user(name, cart, total):
    users[name]["orders"].append({
        "items": cart,
        "total": total,
        "status": "Очікує"
    })
    save_users(users)

def add_favorite(name, item):
    if item not in users[name]["favorites"]:
        users[name]["favorites"].append(item)
    save_users(users)

def show_favorites(name):
    favorites = users[name].get("favorites", [])
    if not favorites:
        print("У тебе ще немає улюблених страв.")
        return
    print("Твої улюблені страви:")
    for item, price in favorites:
        print(f"- {item}: {price} грн")
