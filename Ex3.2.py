def a(number):
    try:
        number = float(number)
        result = 100 / number
        return print(f"Результат деления: {result}")
    except ValueError:
        return "Ошибка: Введено не число."
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно."
    except Exception as o:
        return f"Произошла неизвестная ошибка: {o}."
u_input= input("Введите число для деления на 100: ")
print(a(u_input))