# 1. Сбор данных от пользователя
name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую): ")

# 2. Преобразование типов
age_number = int(age_str)
subjects_list = subjects_str.split(",")

# 3. Создание словаря
student = {
    "name": name,
    "age": age_number,
    "subjects": subjects_list
}

# 4. Красивый вывод анкеты
print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)
print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {student['subjects']}")
print("=" * 30)
