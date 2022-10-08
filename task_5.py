revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))

if revenue > costs:
    print("Прибыль")
    profitability = (revenue - costs) / revenue
    print(f"Прибыльность составляет: {profitability:.3f}")
    staff = int(input("Укажите количество сотрудников: "))
    profit_per_employee = (revenue - costs) / staff
    print(f"Прибыль на сотрудника составляет: {profit_per_employee}")

elif revenue < costs:
    print("Убыток")
else: print("Ноль")
