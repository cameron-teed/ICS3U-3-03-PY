#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# this program gets you to guess my number

import random


def main():
        # this program gets you to guess my number

        # input
        very_secret = random.randint(1, 2+1)

        secret_number = int(input("Try to guess my number: "))

        # process
        if secret_number != very_secret:

                # output
                print("That is not my number, it was {}".format(very_secret))

        # process
        else:

                # output
                print("Thats my number!")


if __name__ == "__main__":
    main()
