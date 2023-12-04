#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("Number:", number, "is positive")
elif number == 0:
    print("Number:", number, "is zero")
else:
    print("Number:", number, "is negative")
