#!/usr/bin/python3
""" FizzBuzz
    Change the if statements to accomodate the challenge
"""
import sys


def fizzbuzz(n):
    """
 FIZZ BUZZ CHALLENGE SOLVED WHERE 3 PRINTS FIZZ AND 5 BUZZ AND 15 FIZZ BUZZ
    """
    if n < 1:
        return

    number_bank = []
    for initial in range(1, n + 1):
        if (initial % 3) == 0 and (initial % 5) == 0:
            number_bank.append("FizzBuzz")
        elif (initial % 3) == 0:
            number_bank.append("Fizz")
        elif (initial % 5) == 0:
            number_bank.append("Buzz")
        else:
            number_bank.append(str(initial))
    print(" ".join(number_bank))
vi

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number_solve = int(sys.argv[1])
    fizzbuzz(number_solve)

