number = int(input('Введите номер места:'))

if 1 <= number <= 36:
    if number % 2 == 0:
        print('Верхнее место')
    else:
        print('Нижнее место')
elif 37 <= number <= 54:
    if number % 2 == 0:
        print('Верхнее боковое место')
    else:
        print('Нижнее боковое место')
else:
    print ('Неверный номер места')


