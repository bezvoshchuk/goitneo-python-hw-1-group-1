from datetime import datetime
from collections import defaultdict 

users = [{"name": "Dmytro", "birthday": datetime(1986, 3, 6)}, 
         {"name": "Petro", "birthday": datetime(1987, 3, 8)}, 
         {"name": "Oleksandra", "birthday": datetime(1990, 3, 14)},
         {"name": "Serhii", "birthday": datetime(2003, 3, 14)},
         {"name": "Oleksandr", "birthday": datetime(1970, 3, 5)}, 
         {"name": "Vitalii", "birthday": datetime(1980, 3, 9)}, 
         {"name": "Oleksii", "birthday": datetime(1989, 3, 8)},  
         {"name": "Svitlana", "birthday": datetime(1996, 3, 11)},
         {"name": "Ivan", "birthday": datetime(1996, 3, 14)},
         {"name": "Vasyl", "birthday": datetime(1998, 3, 5)},
         {"name": "Stepan", "birthday": datetime(2002, 3, 4)},
         {"name": "Ustim", "birthday": datetime(2001, 3, 3)},
         {"name": "Anna", "birthday": datetime(1981, 3, 13)},
         {"name": "Victor", "birthday": datetime(2000, 3, 6)}
         ] 

def get_birthdays_per_week(users):
    result = defaultdict(list) 
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday_this_year = user["birthday"].date().replace(year=today.year)

        if(birthday_this_year < today):
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                   
        delta = (birthday_this_year - today).days       

        if(delta < 7):     
            week_day = birthday_this_year.strftime("%A")              
            if (week_day.lower() in ["saturday", "sunday"]): 
                result['Monday'].append(name)
            else:               
                result[week_day].append(name)

        
    for day, names in result.items():
        print(f"{day}: {names}")             


get_birthdays_per_week(users=users)
