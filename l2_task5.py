numbers1 = [7, 5, 3, 3, 2]
num_input = int(input("Введите число: "))
if num_input > numbers1[0]:
    numbers1.insert(0, num_input)
elif num_input < numbers1[-1]:
    numbers1.append(num_input)
else:
    for i in range(len(numbers1)):
        if num_input > numbers1[i]:
            numbers1.insert(i,num_input)
            break

print(f"Результат: {numbers1}")