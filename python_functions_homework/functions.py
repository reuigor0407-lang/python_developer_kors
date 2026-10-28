def calculate_total(price: int | float, quantity: int) -> int | float:
    """Обчислює загальну вартість замовлення"""
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("Ціна повинна бути числом.")

    if price < 0:
        raise ValueError("Ціна не може бути від'ємною.")

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Кількість повинна бути цілим числом.")

    if quantity < 0:
        raise ValueError("Кількість не може бути від'ємною.")

    return price * quantity


def apply_discount(total: int | float   , discount_percent: int | float =0) -> int | float:
    """Застосовує знижку у відсотках до загальної суми"""
    if isinstance(total, bool) or not isinstance(total, (int, float)):
        raise TypeError("Загальна сума повинна бути числом.")

    if total < 0:
        raise ValueError("Загальна сума не може бути від'ємною.")

    if isinstance(discount_percent, bool) or not isinstance(discount_percent, (int, float)):
        raise TypeError("Знижка повинна бути числом.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Знижка повинна бути від 0 до 100.")

    return total * (1 - discount_percent / 100)


def calculate_statistics(numbers: list[int | float]) -> tuple[int | float, int| float, int| float]:
    """Повертає мінімум, максимум і середнє арифметичне."""
    if not numbers:
        raise ValueError("Послідовність не може бути порожньою.")

    for number in numbers:
        if isinstance(number, bool) or not isinstance(number, (int, float)):
            raise TypeError("Усі елементи повинні бути числами.")

    return min(numbers), max(numbers), sum(numbers) / len(numbers)


def calculate_average(*numbers: int | float) -> float:
    """Обчислює середнє арифметичне довільної кількості чисел"""
    if not numbers:
        raise ValueError("Потрібно передати хоча б одне число.")

    for number in numbers:
        if isinstance(number, bool) or not isinstance(number, (int, float)):
            raise TypeError("Усі аргументи повинні бути числами.")

    return sum(numbers) / len(numbers)


def creat_profile(name, **kwargs: object) -> dict[str, object]:
    """Створює словник профілю користувача"""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Ім'я повинно бути непорожнім рядком.")

    if "age" in kwargs:
        age = kwargs["age"]
        if isinstance(age, bool) or not isinstance(age, int) or age < 0:
            raise ValueError("Вік повинен бути цілим невід'ємним числом.")

    profile = {"name": name}
    profile.update(kwargs)

    return profile


def add_product(name: str, products: list[str] | None = None) -> list[str]:
    """Додає товар до нового або переданого списку"""
    if products is None:
        products = []

    products.append(name)
    return products