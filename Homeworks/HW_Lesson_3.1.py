#                   Частина 3. Базові практичні вправи

# 1. Послідовність чисел

for i in range(1, 101):
    print(i, end=" ")
print()

for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=" ")
print()

for i in range(100, 0, -1):
    print(i, end=" ")
print()

count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(f"Кількість чисел {count}")

# ---------------------------------------------------------
# 2. Сума та середнє арифметичне

n = int(input("Введіть натуральне число: "))

total = 0
even_sum = 0
for i in range(1, n + 1):
    total += i
    if i % 2 == 0:
        even_sum += i
print(f"Сума: {total}")
print("Середнє арифметичне: ", int(total / n))
print(f"Сума парних чисел: {even_sum}")

# --------------------------------------------------------
# 3. Таблиця множення

n = int(input("Введіть число від 1 до 10: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)

for i in range(1, 11):
    j = 1
    while j <= 10:
        print(i, "*", j, "=", i * j)
        j += 1

# -----------------------------------------------------
# 4. Підрахунок цифр

number = int(input("Введіть число: "))

count = 0
digit_sum = 0

if number == 0:
    count = 1
while number > 0:
    count += 1
    digit = number % 10
    digit_sum += digit
    number = number // 10
print("Кількість цифр: ", count)
print("Сума цифр: ", digit_sum)

# ------------------------------------------------------
# 5. Пошук дільників

number = int(input("Введіть додатне число: "))

count = 0
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
        count += 1
print("Кількість дільників:", count)

if number >= 2:
    for i in range(2, number):
        if number % i == 0:
            print(f"Число {number} не є простим")
            break
    else:
        print(f"Число {number} є простим")
else:
    print(f"Число {number} не є простим")

# ---------------------------------------------------
# 6. Система перевірки пароля

correct_password ="password"
attempt = 0
while attempt < 3:
    password = input("Введіть пароль: ")
    if password != correct_password:
        print("Невірний пароль!")
        attempt += 1
        continue
    else:
        print("Доступ дозволено!")
        break
else:
    print("Доступ відмовлено!")

# -----------------------------------------------------
# 7. Меню програми

while True:
    print()
    print("---МЕНЮ---")
    print("1 — Вивести привітання")
    print("2 — Показати числа від 1 до 10")
    print("3 — Обчислити суму від 1 до N")
    print("0 — Вихід")
    command = int(input("Введіть номер команди: "))
    if command == 1:
        print("Доброго дня!")
        continue
    elif command == 2:
        for i in range(1, 11):
            print(i)
        continue
    elif command == 3:
        n = int(input("Введіть число: "))
        total = 0
        for i in range(1, n + 1):
            total += i
        print("Сума чисел:", total)
        continue
    elif command == 0:
        print("Вихід з меню")
        break
    else:
        print("Невідома команда!")
        continue

#------------------------------------------------------
# 8. Геометричні фігури

h = int(input("Введіть висоту: "))
w = int(input("Введіть ширину: "))

for i in range(h):
    for j in range(w):
        print("*", end="")
    print()
print()

for i in range(w):
    for j in range(i + 1):
        print("*", end="")
    print()
print()

for i in range(w):
    for j in range(w - i):
        print("*", end="")
    print()
print()

for i in range(w):
    if i == 0 or i == w - 1:
        print("*" * w)
    else:
        print("*" + " " * (w -2) + "*")
