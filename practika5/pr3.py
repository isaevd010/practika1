USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """
    Конвертирует сумму из долларов США в российские рубли.
    вводит:
        amount_usd (float): Сумма в долларах.
    выводит:
        float: Сумма в рублях.
    """
    return amount_usd * USD_TO_RUB

dollars = float(input("Введите сумму в долларах: "))
rubles = convert_usd_to_rub(dollars)

print(f"{dollars:.2f} USD = {rubles:,.2f} RUB")
