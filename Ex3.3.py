def e():
    a = int(input("Введите число: "))
    b = int(input("Введите месяц: "))
    c = int(input("Введите год. В виде послдених двех цифр: "))
    d = a * b
    if d == c:
        print("Произошла магия!")
    else:
        print("Не магический")
e()