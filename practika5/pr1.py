NALOG = 0.13

income = float(input("Введите ваш годовой доход (руб.): "))

tax_amount = income * NALOG
total_income = income - tax_amount

print(f"Общая сумма дохода: {income:,.2f} руб.")
print(f"Сумма рассчитанного налога: {tax_amount:,.2f} руб.")
print(f"Сумма «на руки» после вычета налога: {total_income:,.2f} руб.")
