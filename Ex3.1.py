def a(number):
    if number %3 == 0:
        return True
    else:
        return False

number = int(input("Введите число "))
if a(number):
    print(f"Число {number} делится на 3.")
else:
    print(f"Число {number} не делиться на 3.")