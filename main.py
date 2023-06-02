from datetime import datetime as dt
from datetime import *

users = [
        {"name":"Bill", "birthday":dt(1995,6,6)},
        {"name":"Stiv", "birthday":dt(1990,6,6)},
        {"name":"Jill", "birthday":dt(1990,6,6)},
        {"name":"John", "birthday":dt(1998,6,6)},
        {"name":"Evgen", "birthday":dt(1992,6,6)},
        {"name":"Jack", "birthday":dt(1980,6,5)},
        {"name":"Ann", "birthday":dt(1964,6,5)},
        {"name":"Helen", "birthday":dt(1999,6,5)},
        {"name":"Max", "birthday":dt(1991,7,5)},
        {"name":"Max", "birthday":dt(1999,7,5)},
        {"name":"Piter", "birthday":dt(1984,6,5)},
        {"name":"Charles", "birthday":dt(1984,6,5)},
        {"name":"German", "birthday":dt(1981,6,5)},
        {"name":"Aaron", "birthday":dt(1992,6,5)},
        {"name":"Alex", "birthday":dt(1993,6,5)},
        {"name":"Alice", "birthday":dt(1998,6,5)},
        {"name":"Andy", "birthday":dt(1997,6,5)},
        {"name":"Bert", "birthday":dt(1994,6,5)},
        {"name":"Bruno", "birthday":dt(1992,6,5)},
        {"name":"Joan", "birthday":dt(1987,6,5)},
        {"name":"Kent", "birthday":dt(1959,6,5)},
        {"name":"Kate", "birthday":dt(1978,6,5)},
        {"name":"Karen", "birthday":dt(1968,6,5)},
        {"name":"Logan", "birthday":dt(1988,6,5)}
]
# Флажок для всвякого. 
flag = 0

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
    return output_of_results(birthday_list)

# Функція яка є частиною output_of_results. 
def fix(weekday, result):
    global flag
    flag += 1
    if flag > 1:
        print('| {:^11} : {:<59}|'.format(' ' * len(weekday), ', '.join(result))) 
    else:
        print('| {:^11} : {:<59}|'.format(weekday, ', '.join(result))) 

# Функція яка виводить результат. 
def output_of_results(birthday_list):
    sums = 0
    result = []
    print('{:^11} '.format(" " + "_"*74 + " "))   
    print('|{:^74}| '.format("Birthday"))
    print('{:^11} '.format("|" + "_"*74 + "|"))
    for weekday, names in birthday_list.items():
        global flag
        if names == []:
            continue
        for name in names:
            sums += len(name)
            result.append(name)
            if sums > 30:   
                fix(weekday, result)
                result.clear()
                sums = 0
        flag = 0
        print('{:^11} '.format("|" + "_"*74 + "|"))

if __name__ == "__main__":
    get_birthdays_per_week(users)
