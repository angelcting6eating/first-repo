import datetime
today = datetime.date.today()
amountofdaysaway = input("How many days away is the thing? ")
# timedelta is a class in the datetime module that represents a duration, the difference between two dates or times. It can be used to perform arithmetic operations on date and time objects, such as adding or subtracting a certain number of days, hours, minutes, etc. In this case, we are creating a timedelta object that represents the number of days specified by the user input.
daysdelta = datetime.timedelta(days=int(amountofdaysaway))
# class datetime.timedelta: A duration expressing the difference between two datetime or date instances to microsecond resolution.
targetdate = today + daysdelta
print("The target date is:", targetdate)
