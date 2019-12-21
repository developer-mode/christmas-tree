from random import randint
from time import sleep

while True:
    print("\033c")

    for x in range(1,30,2):
        rand_row = randint(1, 30)

        if x == 1:
            char = '⭐'
        elif x == 3:
            char = ''
        elif rand_row % 3 == 0:
            char = '❇✯✧'[randint(0,2)]
        elif rand_row % 4 == 0:
            char = '❇✯✧'[randint(0,2)]
        elif rand_row % 5 ==0:
            char = '❇✯✧'[randint(0,2)]
        else:
            char = '='

        print("{:^33}".format(char * x))
    
    print("{:^33}".format("|  |"))
    print("{:^33}".format("|  |"))
    sleep(0.75)

