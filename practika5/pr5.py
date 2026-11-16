B5000 = 5000
B2000 = 2000
B1000 = 1000
B500 = 500
B200 = 200
B100 = 100

amount = int(input("Введите сумму для снятия (кратную 100): "))
remaining = amount

count_5000 = remaining // B5000
remaining = remaining % B5000

count_2000 = remaining // B2000
remaining = remaining % B2000

count_1000 = remaining // B1000
remaining = remaining % B1000

count_500 = remaining // B500
remaining = remaining % B500

count_200 = remaining // B200
remaining = remaining % B200

count_100 = remaining // B100

print(f"\nВыдача суммы {amount} руб.:")
print(f"Купюр по {B5000} руб.: {count_5000} шт.")
print(f"Купюр по {B2000} руб.: {count_2000} шт.")
print(f"Купюр по {B1000} руб.: {count_1000} шт.")
print(f"Купюр по {B500} руб.: {count_500} шт.")
print(f"Купюр по {B200} руб.: {count_200} шт.")
print(f"Купюр по {B100} руб.: {count_100} шт.")
