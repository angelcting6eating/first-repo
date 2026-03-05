
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# question 1
print('Q1:Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk')
answer1 = int(input('Enter your answer (1-2): '))
if answer1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('wrong input')

# question 2
print('Q2) When I’m dead, I want people to remember me as :\n1) The Good \n2)The Great\n3) The Wise \n4) The Bold')
answer2 = int(input('Enter your answer (1-4): '))
if answer2 == 1:
    Hufflepuff += 2
elif answer2 == 2:
    Slytherin += 2.
elif answer2 == 3:
    Ravenclaw += 2.
elif answer2 == 4:
    Gryffindor += 2.
else:
    print('wrong input')

# question 3
print('Q3) Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano\n 4) The drum')
answer3 = int(input('Enter your answer (1-4): '))
if answer3 == 1:
    Slytherin += 4
elif answer3 == 2:
    Hufflepuff += 4
elif answer3 == 3:
    Ravenclaw += 4
elif answer3 == 4:
    Gryffindor += 4
else:
    print('wrong input')

print('Gryffindor:', Gryffindor)
print('Ravenclaw:', Ravenclaw)
print('Hufflepuff:', Hufflepuff)
print('Slytherin:', Slytherin)

if (Gryffindor > Ravenclaw) and (Gryffindor > Hufflepuff) and (Gryffindor > Slytherin):
    print('You are a Gryffindor!')
elif Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print('You are a Ravenclaw!')
elif Hufflepuff > Slytherin:
    print('You are a Hufflepuff!')
else:
    print('You are a Slytherin!')
