import matplotlib.pyplot as plt
import random
plt.ion()

def roll_hundred_pair():
    total = []
    for choice in range(100):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total += [(dice1+dice2)]
    plt.pie(total)
    plt.show()
