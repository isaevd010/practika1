import math
x = float(input("градусы х "))
total = math.sin(x) + math.cos(x) + math.tan(x)**2
total = math.radians(total)
print(total)
