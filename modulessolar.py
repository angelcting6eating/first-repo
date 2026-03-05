from math import pi
from random import choice as ch

planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]

random_planet = ch(planets)


def calculate_area():
    if random_planet == 'Mercury':
        r = 2440
    elif random_planet == 'Venus':
        r = 6052
    elif random_planet == 'Earth':
        r = 6371
    elif random_planet == 'Mars':
        r = 3390
    elif random_planet == 'Saturn':
        r = 58232
    else:
        print("Oops! An error occurred")
        return

    area = 4 * pi * r**2
    print(f"The surface area of {random_planet} is {area:.2f} km²")


calculate_area()
