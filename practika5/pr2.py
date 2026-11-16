weight, height = map(float, input("Введите ваш вес в кг и рост в м через пробел: ").split())
bmi = weight / (height * height)

print(f"Ваш индекс массы тела = {bmi:.1f}")
