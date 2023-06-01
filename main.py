from datetime import datetime as dt
from datetime import *

# users = [
#         {"name":"Bill", "birthday":dt(1995,1,13)},
#         {"name":"Stiv", "birthday":dt(1990,1,6)},
#         {"name":"Jill", "birthday":dt(1990,2,20)},
#         {"name":"John", "birthday":dt(1998,2,23)},
#         {"name":"Evgen", "birthday":dt(1992,3,11)},
#         {"name":"Jack", "birthday":dt(1980,3,21)},
#         {"name":"Ann", "birthday":dt(1964,4,17)},
#         {"name":"Helen", "birthday":dt(1999,4,1)},
#         {"name":"Max", "birthday":dt(1991,5,3)},
#         {"name":"Max", "birthday":dt(1999,5,31)},
#         {"name":"Piter", "birthday":dt(1984,6,6)},
#         {"name":"Charles", "birthday":dt(1984,6,7)},
#         {"name":"German", "birthday":dt(1981,7,27)},
#         {"name":"Aaron", "birthday":dt(1992,7,15)},
#         {"name":"Alex", "birthday":dt(1993,8,12)},
#         {"name":"Alice", "birthday":dt(1998,8,17)},
#         {"name":"Andy", "birthday":dt(1997,9,13)},
#         {"name":"Bert", "birthday":dt(1994,9,11)},
#         {"name":"Bruno", "birthday":dt(1992,10,5)},
#         {"name":"Joan", "birthday":dt(1987,10,27)},
#         {"name":"Kent", "birthday":dt(1959,11,22)},
#         {"name":"Kate", "birthday":dt(1978,11,21)},
#         {"name":"Karen", "birthday":dt(1968,12,5)},
#         {"name":"Logan", "birthday":dt(1988,12,9)}
# ]

users = [
        {"name":"Bill", "birthday":dt(1995,6,13)},
        {"name":"Stiv", "birthday":dt(1990,6,6)},
        {"name":"Jill", "birthday":dt(1990,6,20)},
        {"name":"John", "birthday":dt(1998,6,23)},
        {"name":"Evgen", "birthday":dt(1992,6,11)},
        {"name":"Jack", "birthday":dt(1980,6,21)},
        {"name":"Ann", "birthday":dt(1964,6,17)},
        {"name":"Helen", "birthday":dt(1999,6,2)},
        {"name":"Max", "birthday":dt(1991,7,3)},
        {"name":"Max", "birthday":dt(1999,7,27)},
        {"name":"Piter", "birthday":dt(1984,6,3)},
        {"name":"Charles", "birthday":dt(1984,6,4)},
        {"name":"German", "birthday":dt(1981,6,27)},
        {"name":"Aaron", "birthday":dt(1992,6,15)},
        {"name":"Alex", "birthday":dt(1993,6,12)},
        {"name":"Alice", "birthday":dt(1998,6,17)},
        {"name":"Andy", "birthday":dt(1997,6,13)},
        {"name":"Bert", "birthday":dt(1994,6,11)},
        {"name":"Bruno", "birthday":dt(1992,6,5)},
        {"name":"Joan", "birthday":dt(1987,6,27)},
        {"name":"Kent", "birthday":dt(1959,6,22)},
        {"name":"Kate", "birthday":dt(1978,6,21)},
        {"name":"Karen", "birthday":dt(1968,6,5)},
        {"name":"Logan", "birthday":dt(1988,6,9)}
]
# Словник, число/день тижня.
weekday_list = { "0": "Monday", "1": "Tuesday", "2": "Wednesday", "3": "Thursday", "4": "Friday", "5": "Saturday","6": "Sunday"}

# Словник, день тижня/ ім'я.
birthday_list = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}

# Сьогодні. 
today = dt.now()

# Через тиждень.
next_week = datetime(year=today.year, month=today.month, day=today.day+7)

# Функція яка перевіряє в кого день народження на протязі наступної неділі.
def get_birthdays_per_week(users):
    for user in users:
        date_u = user["birthday"] 
        date = datetime(year=today.year, month=date_u.month, day=date_u.day) 
        if date > today and date < next_week: # Перевіряє чи є впродовж тижня в цієї людини день народження.
            if weekday_list[str(date.weekday())] not in ["Saturday", "Sunday"]: # Перевіряє чи випадає день народження на суботу неділю.
                birthday_list[weekday_list[str(date.weekday())]].append(user["name"])
            else: # Якщо випадає на суботу/неділю додає до понеділка.
                birthday_list[weekday_list["0"]].append(user["name"])
    return result(birthday_list)

# Функція яка виводить результат. 
def result(birthday_list):
    # print('{:^10} '.format(" " + "_"*113 + " "))  # Табличка працює не у всіх (╯ ° □ °) ╯ (┻━┻)
    # print('|{:^113}| '.format("Birthday"))
    for weekday, names in birthday_list.items():
        if names == []:
            continue
        # print('{:^10} '.format("|" + "_"*113 + "|"))
        print('{:<10} : {:<100}'.format(weekday, ', '.join(names))) # print('|{:<10} : {:<100}|'.format(weekday, ', '.join(names)))
    # print('{:^10} '.format("|" + "_"*113 + "|"))

if __name__ == "__main__":
    get_birthdays_per_week(users)
