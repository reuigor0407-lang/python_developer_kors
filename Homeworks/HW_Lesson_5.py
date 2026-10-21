#           Блок 1: Теоретичний бліц (5 питань)

# 1. Кортеж (1, 2, [3, 4]) не можна використовувати яе елемент множини set або ключ словника dict
#   тому що він містить список, а список є змінним та нехешованим типом даних, тому весь кортеж теж є нехешованим

# 2. Колізія в хеш-таблиці виникає, коли різні ключі мають однакове хеш-значення. Python розв'язує колізії
#   за допомогою спеціального механізму пошуку та перевірки ключів на рівність.

# 3. collections.UserDict рекомендується використовувати для створення власних класів словників, тому що він є
#  зручною обгорткою над словником і полегшує перевизначення методів.

# 4. Словники dict порівнюють за парами ключ-значення незалежно від порядку їх додавання.
#   Об'єкти collections.OrderedDict порівнюють з урахуванням порядку елементів, якщо порівнюються між собою.
#   Тому два OrderedDict з однаковими парами, але різним порядком, не є рівними.

# 5. Для list перевірка x in data має часову складність O(n)б оскільки елементи перевіряються послідовно.
#   Для set середня часова складність становить О(1), тому що множина використовує хешування.
# ------------------------------------------------------

#           Блок 2: Практичні завдання

# Завдання 1: очищення списку від дублікатів та аналіз логів (set)

day1_users = ["alice", "bob", "charlie", "david", "alice", "eva"]
day2_users = ["bob", "frank", "eva", "george", "charlie", "charlie"]

set1 = set(day1_users)
set2 = set(day2_users)

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
# --------------------------------------------

# Завдання 2: Пошук унікальних замовлень без урахування порядку (frozenset)

orders = [
    ["хліб", "молоко"],
    ["молоко", "хліб"],
    ["сік", "хліб"],
    ["хліб", "молоко"]
]

frozen_orders = [frozenset(order) for order in orders]

unique_orders = set(frozenset(order) for order in orders)
print(unique_orders)
print(len(unique_orders))
# ------------------------------------------

# Завдання 3: групування за категоріями (defaultdict)

from collections import defaultdict

orders_data = [
    ("Електроніка", "Ноутбук"),
    ("Їжа", "Яблуко"),
    ("Електроніка", "Смартфон"),
    ("Їжа", "Хліб"),
    ("Одяг", "Сорочка"),
    ("Їжа", "Молоко")
]

grouped_orders = defaultdict(list)

for category, product in orders_data:
    grouped_orders[category].append(product)

print(dict(grouped_orders))
# ------------------------------------------

# Завдання 4: аналіз частоти слів у тексті (Counter)

from collections import Counter

text = "python python java python c++ java python c++ javascript"

words = text.split()

language_counts = Counter(words)
print(language_counts)
print(language_counts.most_common(2))
# ----------------------------------------------

# Завдання 5: налаштування програми з декількох джерел (ChainMap)

from collections import ChainMap

default_config = {"theme": "light", "language": "uk", "font_size": 12}
user_config = {"theme": "dark", "font_size": 16}

config = ChainMap(user_config, default_config)

print(config["theme"])
print(config["font_size"])
print(config["language"])
# ---------------------------------------------

# Завдання 6: робота з порядком та керування елементами (OrderedDict)

from collections import OrderedDict

data = OrderedDict([("a", 1), ("b", 2), ("c", 3), ("d", 4)])

data.move_to_end("a")

first_item = data.popitem(last=False)
print(first_item)
print(list(data.keys()))