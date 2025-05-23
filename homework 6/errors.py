users = {
    "nick": "12-16",
    "ann": "16-18",
    "vlad": "18-21",
    "artem": "21-25"
}

name = input("Введіть ім'я користувача: ")

try:
    print(f"Вікова група користувача {name}: {users[name]}")
except KeyError:
    print("Користувача з таким ім'ям не знайдено.")
