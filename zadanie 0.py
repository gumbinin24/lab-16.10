first = list(input("Введите список чисел \n"))
res = list()
for i in range(1, len(first)):
    if first[i-1] < first[i]:
        res.append(first[i])
print(*res)

