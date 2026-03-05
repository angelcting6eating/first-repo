# Slot Machine 🎰
# Codédex

import random

symbols = [
    '🍒',
    '🍇',
    '🍉',
    '7️⃣'
]


def play():

    for i in range(1, 5):
        results = random.choices(symbols, k=3)
        print(results)

        if results == ['7️⃣', '7️⃣', '7️⃣']:
            print('Jackpot!!! 💰')
            break
        else:
            results = random.choices(symbols, k=3)


answer = ''
while answer.upper() != 'N':
    play()
    answer = input('Keep playing? (Y/N) ')

print('Thanks for playing!')
