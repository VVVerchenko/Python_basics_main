month = int(input("Введите порядковый номер месяца (1...12): "))

seasons_list = ["зима", "зима", "весна", "весна", "весна", "лето",
                "лето", "лето", "осень", "осень", "осень", "зима"]

seasons_dict = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето",
                7: "лето", 8: "лето", 9: "осень", 10: "осень", 11: "осень", 12: "зима"}

print(seasons_list[month - 1])
print(seasons_dict.get(month))
