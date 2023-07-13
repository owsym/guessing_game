import random

jackpot = random.randint(1, 100)

guess = int(input('chal guess kar : '))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print('thora barha, ')
    else:
        print('thora kam kr, ')
    guess = int(input('chal guess kar : '))
    counter += 1

print('Sahi jawab,')
print('you took', counter, 'attempts')
