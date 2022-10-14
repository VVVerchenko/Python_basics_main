list1 = []
for i in range(7):
    list1.append(input(f"Введите {i}-й элемент списка: "))

list2 = list1.copy()

for i in range(len(list1)):
    if i % 2 == 0 and len(list1) % 2 == 0:
        list2[i] = list1[i+1]
    elif i % 2 == 1 and len(list1) % 2 == 0:
        list2[i] = list1[i-1]
    else:
        if i % 2 == 0 and list1[i] != list1[-1] and len(list1) % 2 != 0:
            list2[i] = list1[i + 1]
        elif i % 2 == 1 and list1[i] != list1[-1] and len(list1) % 2 != 0:
            list2[i] = list1[i - 1]
        else:
            list2[i] = list1[i]

list1 = list2
print(list1)


