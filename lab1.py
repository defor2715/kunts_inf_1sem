def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

user_input = input("Введите год")

if user_input.isdigit():
    year = int(user_input)
    print("Високосный" if leap_year(year) else "Не високосный")
else:
    print("Ошибка")