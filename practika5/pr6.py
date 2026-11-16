def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между двумя точками.

    вводит:
        x1, y1 (float): Координаты первой точки.
        x2, y2 (float): Координаты второй точки.
    выводит:
        float: Расстояние между точками.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по трем сторонам (формула Герона).

    вводит:
        a, b, c (float): Длины сторон треугольника.
    выводит:
        float: Площадь треугольника.
    """
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

x1, y1 = map(float, input("Введите координаты точки A (x1 y1) через пробел: ").split())
x2, y2 = map(float, input("Введите координаты точки B (x2 y2) через пробел: ").split())
x3, y3 = map(float, input("Введите координаты точки C (x3 y3) через пробел: ").split())

side_1 = calculate_distance(x1, y1, x2, y2)
side_2 = calculate_distance(x2, y2, x3, y3)
side_3 = calculate_distance(x3, y3, x1, y1)

area = calculate_triangle_area(side_1, side_2, side_3)

print(f"Площадь треугольника равна: {area:.2f}")
