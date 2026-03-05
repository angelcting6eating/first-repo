menu = {
    1: "Cheeseburger",
    2: "Fries",
    3: "Soda",
    4: "Ice Cream",
    5: "Cookie"}


def get_item(option):
    return menu.get(option, "Sorry, that item is not on the menu.")


def welcome():
    print("Welcome! Here is the menu:")
    for key, value in menu.items():
        print(f"{key}: {value}")


welcome()

option = int(input("What would you like to order? "))
print(get_item(option))

# or, model answer:

def get_item(x):
  if x == 1:
    return '🍔 Cheeseburger'
  elif x == 2:
    return '🍟 Fries'
  elif x == 3:
    return '🥤 Soda'
  elif x == 4:
    return '🍦 Ice Cream'
  elif x == 5:
    return '🍪 Cookie'
  else:
    return "invalid option"

def welcome():
  print('Welcome to Sonnyboy\'s Diner!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))