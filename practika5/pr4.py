PI = 3.14159

def calculate_rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника по его ширине и высоте.
    вводит:
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.
    выводит:
        float: Площадь прямоугольника.
    """
    return width * height

def calculate_circle_area(radius):
    """
    Вычисляет площадь круга по его радиусу.
    вводит:
        radius (float): Радиус круга.
    выводит:
        float: Площадь круга.
    """
    return PI * (radius ** 2)

rect_width, rect_height = map(float, input("Введите ширину и высоту прямоугольника через пробел: ").split())
rect_area = calculate_rectangle_area(rect_width, rect_height)
print(f"Площадь прямоугольника: {rect_area:.2f}")

circle_radius = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(circle_radius)
print(f"Площадь круга: {circle_area:.2f}")
