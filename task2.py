time_sec_inp = input("Введите время в секундах: ")

if time_sec_inp.isdigit():
    time_sec_inp = int(time_sec_inp)
    time_hours = time_sec_inp // 3600
    time_minutes = (time_sec_inp - time_hours * 3600) // 60
    time_seconds = (time_sec_inp - time_hours * 3600 - time_minutes * 60)

    if time_hours < 10:
        time_hours_str = "0" + str(time_hours)
    else:
        time_hours_str = str(time_hours)
    if time_minutes < 10:
        time_minutes_str = "0" + str(time_minutes)
    else:
        time_minutes_str = str(time_minutes)
    if time_seconds < 10:
        time_seconds_str = "0" + str(time_seconds)
    else:
        time_seconds_str = str(time_seconds)

    print(f"Время: {time_hours_str}:{time_minutes_str}:{time_seconds_str}")

else:
    print("Ошибка ввода!!!")
