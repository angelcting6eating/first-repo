import datetime
import bday_message
today = datetime.date.today()
next_birthday = datetime.date(2026, 3, 19)
days_away = next_birthday - today

if today == next_birthday:
    random_message()
else:
    print(f"My next birthday is {days_away}  away!")
