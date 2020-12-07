#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a dating program.


def main():
    # This is the function to play dating program.

    # Input
    userinput = input("Enter your age:")
    print("")

    # Process & output
    try:
        userinput = int(userinput)
        if 25 <= userinput <= 40:
            print("You can date my grandchild")
        else:
            print("You can not date my grandchild!!!")
    except Exception:
        print("You are not type in an integer!")


if __name__ == "__main__":
    main()
