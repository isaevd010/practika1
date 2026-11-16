num = int(input("Введите  положительное четырёхзначное целое число: " ))
thousands = num // 1000
hundreds = ((num - thousands * 1000)  // 100)
tens = (num // 10) % 10
one = num % 10
print("Цифра в позиции тысяч равна ", thousands)
print("Цифра в позиции сотен равна ", hundreds)
print("Цифра в позиции десятков равна ", tens)
print("Цифра в позиции единиц равна ", one)
