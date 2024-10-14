def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def devide(x,y):
    if y != 0:
        return x / y
    else:
        print('Ошибка, на ноль делить нельзя')


print('Выберите математическую операцию')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')

user_choice = input('Введите номер операции: ')

number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))

if user_choice == '1':
    print(f"Результат: {add(number1, number2)}")
elif user_choice == '2':
    print(f"Результат: {subtract(number1, number2)}")
elif user_choice == '3':
    print(f"Результат: {multiply(number1, number2)}")
elif user_choice == '4':
    print(f"Результат: {devide(number1, number2)}")
else:
    print("Неверный ввод")

