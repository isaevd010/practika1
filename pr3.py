num1= int(input("Введите первое число: "))
num2= int(input("Введите второе число: "))

try:
   sum = num1 + num2
   print("Сумма:",sum)
except ValueError:
    print("Ошибка: нужно ввести корректные целые1/ числа.")