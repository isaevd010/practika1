school = int(input("школьники "))
mandarin = int(input("мандарины "))
balance = mandarin // school
left = mandarin % school
print(balance, "каждому ")
print(left, "осталось ")
