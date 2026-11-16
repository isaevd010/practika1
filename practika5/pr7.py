FUEL_PRICE = 49.5
KM_PER_UNIT = 100

def calculate_trip_cost(distance_km, fuel_consumption):
    """
    Рассчитывает необходимое количество топлива и стоимость поездки.

    вводит:
        distance_km (float): Расстояние поездки в километрах.
        fuel_consumption (float): Расход топлива на 100 км (в литрах).
    выводит:
        tuple: Кортеж из двух чисел (необходимые литры топлива, общая стоимость).
    """
    total_liters = distance_km * (fuel_consumption / KM_PER_UNIT)
    total_cost = total_liters * FUEL_PRICE
    return total_liters, total_cost

distance, consumption = map(
    float,
    input("Введите расстояние (км) и расход топлива на 100 км через пробел: ").split()
)

liters_needed, trip_cost = calculate_trip_cost(distance, consumption)

print(f"Необходимо бензина: {liters_needed:.2f} л.")
print(f"Стоимость поездки: {trip_cost:.2f} руб.")
