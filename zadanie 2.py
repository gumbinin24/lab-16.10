first = list(input("Введите первый список чисел \n"))
second = list(input("Введите второй список чисел \n"))
counter = 0
for i in first:
    if i in second:
        counter += 1
print(counter)
