#                                   Рівень 6. Підсумковий проєкт
#       Завдання 17. Система керування доступом до навчальної платформи

VIEW_COURSES = 1
SUBMIT_HOMEWORK = 2
VIEW_CERTIFICATES = 4
MANAGE_USERS = 8

age = 20
is_authenticated = True
is_active = True
is_blocked = False
is_premium = False
is_admin = False

if age < 16:
    print("Вам повинно бути не менше 16 років")
if not is_authenticated:
    print("Потрібна авторизація")
if is_blocked:
    print("Заблокований акаунт")
if not is_active:
    print("Неактивований користувач")

access = age >= 16 and is_authenticated and is_active and not is_blocked

if is_blocked:
    role = "blocked"
    print("Статус: Заблокований акаунт")
elif not is_authenticated:
    role = "guest"
    print("Статус: Гість")
elif not access:
    role = "denied"
    print("Доступ заборонено")
else:
    if is_admin:
        role = "admin"
        print("Роль: Адміністратор")
    elif is_premium:
        role = "premium"
        print("Роль: Преміум користувач")
    else:
        role = "user"
        print("Роль: Звичайний користувач")

if role == "guest":
    permission = VIEW_COURSES
elif role == "user":
    permission = VIEW_COURSES | SUBMIT_HOMEWORK
elif role == "premium":
    permission = VIEW_COURSES | SUBMIT_HOMEWORK | VIEW_CERTIFICATES
elif role == "admin":
    permission = VIEW_COURSES | SUBMIT_HOMEWORK | VIEW_CERTIFICATES | MANAGE_USERS
else:
    permission = 0

if access:
    print("--- МЕНЮ ---")
    print("courses      - переглянути курси")
    print("homework     - здати домашнє завдання")
    print("certificates - переглянути сертифікати")
    print("users        - керування користувачами")
    print("help         - допомога")
    print("exit         - вихід")

    command = input("Введіть команду: ").strip().lower()

    match command:
        case "courses":
            if permission & VIEW_COURSES:
                print("Доступ дозволено: перегляд курсів")
                print("Команда виконана успішно.")
            else:
                print("Відмова: недостатньо прав")
        case "homework":
            if permission & SUBMIT_HOMEWORK:
                print("Доступ дозволено: здати домашнє завдання")
                print("Команда виконана успішно.")
            else:
                print("Відмова: недостатньо прав")
        case "certificates":
            if permission & VIEW_CERTIFICATES:
                print("Доступ дозволено: переглянути сертифікати")
                print("Команда виконана успішно.")
            else:
                print("Відмова: недостатньо прав")
        case "users":
            if permission & MANAGE_USERS:
                print("Доступ дозволено: керування користувачами")
                print("Команда виконана успішно.")
            else:
                print("Відмова: недостатньо прав")
        case "help":
            print("Введіть назву команди з меню")
        case "exit":
            print("Вихід з системи")
        case _:
            print("Невідома команда")
else:
    print("Меню недоступне: доступ заборонено")

# -------------------- ТЕСТУВАННЯ -------------------------

  # №     Сценарій                        Очікуваємий результат                         Перевірка
  #
  # 1     Звичайний користувач            Доступ до курсів та д/з                       Працює коректно
  # 2     Преміум                         Доступ до курсів, д/з та сертифікатів         Працює коректно
  # 3     Адміністратор                   Доступ до всіх команд                         Працює коректно
  # 4     Неавторизований користувач      Статус гість, доступ заборонено               Працює коректно
  # 5     Заблокований акаунт             Доступ заборонено                             Працює коректно
  # 6     Неактивний акаунт               Доступ заборонено                             Працює коректно
  # 7     Вік менше 16 років              Доступ заборонено                             Працює коректно
  # 8     без необхідного дозволу         Недостатньо прав                              Працює коректно
  # 9     Невідома команда                Невідома команда                              Працює коректно
  # 10    Дозволена команда               Доступ дозволено. Команда виконана успішно    Працює коректно