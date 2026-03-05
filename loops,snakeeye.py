import random
notsnakeeyes = True

while notsnakeeyes:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    if total == 2:
        notsnakeeyes = False
        print('Snake eyes!')
    else:
        print('Nope')


# alternatively, i can use this which is a bit simpler, idk why i was being dense

while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    if total == 2:
        print('Snake eyes!')
        break
    else:
        print('Nope')

# total never changes inside the loop, so the condition while total != 2 is always true once it starts.
# i just need to make sure the total is in the loop


# ACTUAL ANSWER: this is what they wanted me to do,
# i guess the instruction did say (First, use the random module to “roll” the two dice.)
# they just wanted me to roll the dice before the loop starts, this also has less variables


die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

while total != 2:
    print('Nope')
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

print('Snake eyes')
