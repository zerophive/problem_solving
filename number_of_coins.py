#!/usr/bin/env python3

# came across this here: https://www.youtube.com/watch?v=HWW-jA6YjHk
# it only took me 20 minutes to come up with this
# then I got bored I did not watch to the end, but this should cover most of the use cases

import sys

def num_of_coins(amount):
    coins = {
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }

    def myMod(number, modulo):
        if number % modulo == 0:
            return int(number / modulo), 0

        whole_value = int(number / modulo)
        remainder = number % modulo

        return whole_value, remainder

    if amount == 0: return amount

    num_of_coins = 0
    remainder = amount
    for name,coin in coins.items():
        whole_coins, remainder = myMod(remainder, coin)
        if whole_coins != 0:
            num_of_coins += whole_coins
            print(str(whole_coins) + " " + name)
        if remainder == 0: break

    return num_of_coins

#print(num_of_coins(25))
print("total number of coins: " + str(num_of_coins(int(sys.argv[1]))))
