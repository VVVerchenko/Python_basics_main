data = [
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}),
(4, {'название': 'монитор', 'цена': 15000, 'количество': 3, 'eд': 'шт.'})
]

dict1 = data[0][1]

dicts = []
for d in range(len(data)):
    dicts.append(data[d][1])

keys1 = list(dict1.keys())

results = []
for k in range(len(keys1)):
    results.append([])

for e in range(len(dict1)):
    for i in range(len(data)):
        results[e].append(dicts[i][keys1[e]])

result_dict = {}
for p in range(len(keys1)):
    result_dict[keys1[p]] = results[p]

for pr in range(len(keys1)):
    print(f"{keys1[pr]}: {result_dict[keys1[pr]]}")