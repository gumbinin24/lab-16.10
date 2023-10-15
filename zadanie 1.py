lst = list(input("Введите список чисел \n"))
lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
print(lst)


