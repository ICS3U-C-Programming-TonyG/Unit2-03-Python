#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-03-04

# Calculates the subtotal as well as the total of a pizza

def main():
    # Asks for diameter and displays diameter in inches
    diameter_inch = float(input("What is the diameter in inches of the pizza you desire?:"))
    print("diameter in inches is:" + str(diameter_inch))

    # Calculates and displays subtotal
    print("The total without tax is:{:.2f}".format (4.25 + 1.5 * diameter_inch))

    # Calculates and displays the total with tax, also defines HST
    HST = 0.13
    print("the total with tax is:{:.2f}".format (4.25 + 1.5 * diameter_inch + HST * (4.25 + 1.5 * diameter_inch)))

if __name__ == "__main__":
    main()
