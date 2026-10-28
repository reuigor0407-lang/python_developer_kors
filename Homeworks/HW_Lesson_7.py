#           Рівень 1: Базовий (функції як об'єкти, анонімні, чисті функції)

# Завдання 1.1. Робота зі списками за допомогою lambda, map та sorted

products = [
    {"name": "Смартфон", "price": 12000, "category": "Електроніка"},
    {"name": "Навушники", "price": 1500, "category": "Електроніка"},
    {"name": "Книга", "price": 350, "category": "Освіта"},
    {"name": "Рюкзак", "price": 2500, "category": "Аксесуари"},
    {"name": "Ручка", "price": 50, "category": "Освіта"},
]

sorted_products = sorted(products, key=lambda x: (x["price"], x["name"]))
for product in sorted_products:
    print(f'{product["name"]}: {product["price"]}: {product["category"]}')

print(list(filter(lambda x: x["category"] == "Освіта", products)))

print(list(product["name"].upper() for product in products))

# Завдання 1.2. Чисті функції


def calculate_final_price(base_price: float, discount_percent: float) -> float:
    return base_price * (1 - discount_percent / 100)


#           Рівень 2: Середній (рекурсивні алгоритми та їх види)

# Завдання 2.1. Рекурсивний обхід вкладених структур


def sum_nested_list(nested_list) -> int:
    total = 0

    for item in nested_list:
        if isinstance(item, list):
            total += sum_nested_list(item)
        else:
            total += item
    return total


data = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sum_nested_list(data))

# Завдання 2.2. Хвостова рекурсія


def sum_of_input_numbers(n: int, total: int=0) -> int:
    if n == 0:
        return total
    return sum_of_input_numbers(n - 1, total + n)


print(sum_of_input_numbers(10))

#           Рівень 3: Просунутий (каррирування та архітектура)
# Завдання 3.1. Реалізація каррирування


def calculate_order_cost(tax_rate):
    def shipping_cost(cost):
        def base_price(price):
            return price + (price * tax_rate) + cost
        return base_price
    return shipping_cost


print(calculate_order_cost(0.2)(100)(2500))

from functools import partial
order_with_tax = calculate_order_cost(0.2)
order_with_delivery = order_with_tax(100)
special_order = partial(order_with_delivery)
print(special_order(2500))

# Завдання 3.2. Архітектурна декомпозиція бізнес-логіки


def calculate_base_pay(hours_worked: int | float, hourly_rate: float) -> float:
    return hours_worked * hourly_rate


def apply_bonus(base_pay: float, performance_rating: str) -> float:
    return base_pay * 1.2 if performance_rating == "A" else base_pay * 1.1 if performance_rating == "B" else base_pay


def deduct_taxes(total_pay: float, tax_percent: int | float) -> float:
    return total_pay * tax_percent / 100


def calculate_employee_net_pay(hours_worked: int | float, hourly_rate: float, performance_rating: str, tax_percent: int | float) -> float:
   salary = calculate_base_pay(hours_worked, hourly_rate)
   salary_with_bonus = apply_bonus(salary, performance_rating)
   tax = deduct_taxes(salary_with_bonus, tax_percent)
   return salary_with_bonus - tax


print(calculate_employee_net_pay(160, 220, "A", 25))



