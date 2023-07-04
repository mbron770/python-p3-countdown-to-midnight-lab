# your code goes here!
from time import sleep


def countdown(x):
    # while x > 0:
    #     print(f'{x} SECOND(S)!')
    #     x-=1
    # print('HAPPY NEW YEAR!')

    for x in range(x, 0, -1):
        print(f'{x} SECOND(S)!')
    print('HAPPY NEW YEAR!')


def countdown_with_sleep(x):
    # while x > 0:
    #     print(f'{x} SECOND(S)!')
    #     sleep(1)
    #     x-=1
    # print('HAPPY NEW YEAR!')

    for x in range(x, 0, -1):
        print(f'{x} SECOND(S)!')
        sleep(1)
    print('HAPPY NEW YEAR!')
