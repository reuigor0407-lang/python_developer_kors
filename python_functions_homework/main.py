from functions import (calculate_total, apply_discount, calculate_statistics, calculate_average, creat_profile, add_product)


def main():
    # Завдання 1.1: Обчислення загальної вартості
    print("Завдання 1.1: Загальна вартість")
    print(calculate_total(250, 3)) # 750
    print(calculate_total(100, 0)) # 0

    # Завдання 1.2: Розрахунок знижки
    print("\nЗавдання 1.2: Розрахунок знижки")
    print(apply_discount(1000)) # 1000
    print(apply_discount(1000, 10)) # 900
    print(apply_discount(500, 100)) # 0

    # Завдання 1.3: Обчислення статистики
    print("\nЗавдання 1.3: Обчислення статистики")
    minimum, maximum, average = calculate_statistics([10, 20, 30])
    print("Мінімум: ", minimum)
    print("Максимум: ", maximum)
    print("Середнє арифметичне", average)

    # Перевірка некоректних аргументів
    print("\nПеревірка некоректних даних")

    test_cases = [
        (calculate_total, (-10, 2)),
        (calculate_total, (100, 2.5)),
        (apply_discount, (500, 120)),
        (calculate_statistics, ([],)),
    ]

    for function, arguments in test_cases:
        try:
            function(*arguments)
        except (TypeError, ValueError) as error:
            print(f"{function.__name__}: {error}")


# Завдання 2.1: Гнучкий калькулятор
    print("\nЗавдання 2.1: Середнє арифметичне")
    print(calculate_average(10, 20, 30))
    print(calculate_average(5, 15))

    try:
        calculate_average()
    except ValueError as error:
        print("Помилка: ", error)

    try:
        calculate_average(10, [20, 30])
    except TypeError as error:
        print("Помилка: ", error)

# Завдання 2.2: Створення профілю
    print("\nЗавдання 2.2: Профіль користувача")

    profile = creat_profile(
        "Олена",
        age=22,
        city="Львів",
        profession="Python Developer"
    )
    print(profile)

    # Розпакування словника через **
    data = {"age": 25, "city": "Київ"}
    print(creat_profile("Андрій", **data))

    # Перевірка некоректних даних
    try:
        creat_profile("", age=-5)
    except ValueError as error:
        print("Помилка: ", error)

    # Завдання 3.1: Аналіз області видимості
    print("\nЗавдання 3.1: Аналіз коду")

    # Приклад А: число не змінюється
    def change_number(value):
        value = 100

    number = 10
    change_number(number)
    print("Приклад А: ", number)

    # Приклад В: список змінюється через append()
    def change_list(items):
        items.append(100)
    numbers = [10, 20]
    change_list(numbers)
    print("Приклад В: ", numbers)

    # Приклад С: локальна змінна отримує новий список
    def replace_list(items):
        items = [100, 200]

    numbers = [10, 20]
    replace_list(numbers)
    print("Приклад С: ", numbers)


    # Завдання 3.2: Перевірка незалежності списків
    print("\nЗавдання 3.2: Безпечне додавання товарів")

    first = add_product("Яблуко")
    second = add_product("Банан")

    assert first == ["Яблуко"]
    assert second == ["Банан"]
    assert first is not second

    existing = ["Хліб"]
    result = add_product("Молоко", existing)
    assert result == ["Хліб", "Молоко"]

    print("Усі три тести пройдено успішно!")


    # Завдання 3.3: Правило LEGB
    print("\nЗавдання 3.3: Правило LEGB")

    message = "Глобальний рівень"

    def outer():
        message = "Зовнішній рівень"

        def inner():
            message = "Локальний рівень"
            print("Local:", message)

        inner()
        print("Enclosing:", message)

    outer()
    print("Global:", message)
    print("Built-in:", len([10, 20, 30]))


if __name__ == "__main__":
    main()