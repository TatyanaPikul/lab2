a=int(input("Введите номер места от 1 до 54 включительно"))

if a <=36:
    print("Место в купе")
    if a % 2 == 0:
        print("верхнее")
    else:
        print("нижнее")
if a>35 and a<55:
    print("Место боковое")
    if a % 2 == 0:
        print("верхнее")
    else:
        print("нижнее")