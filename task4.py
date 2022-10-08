input_num = int(input("Введите целое положительное число: "))

max_number = 0
current_num = 1

while current_num > 0:
    current_num = input_num % 10
    if current_num > max_number:
        max_number = current_num
    else:pass
    input_num = input_num // 10

print(max_number)
