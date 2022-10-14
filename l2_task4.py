text_inp = input("Введите текст: ")

list1 = text_inp.split()
for i, v in enumerate(list1,1):
    print(f'{i}) {v[0:10]}')

