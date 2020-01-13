#!/usr/bin/env python3
"""
@author MrDent0n
@brief small test script to
"""

while True:
    answer = input("Do you want to exit the loop? [y/N]:")
    if answer == "" or answer.lower() == "n":
        continue
    elif answer.lower() == "y":
        break
    else:
        print("I am sorry, {} made no sense to me, reply with only Y or N" .format(answer))



print("Thank you, come again...")