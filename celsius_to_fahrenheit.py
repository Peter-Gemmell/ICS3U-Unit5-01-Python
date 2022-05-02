#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on May 2022
# This program uses fahrenheit function


def fahrenheit():
    # celcius to fahrenheit

    celcius_string = input("Enter the temperature in Celsius : ")

    try:
        celcius = int(celcius_string)
        fahrenheit = round((celcius * 9 / 5) + 32, 2)

        print("{}°C is {}°F".format(celcius, fahrenheit))
    except Exception:
        print("Invalid temperature entered, please try again.")


def main():
    fahrenheit()
    print("\nDone.")


if __name__ == "__main__":
    main()
