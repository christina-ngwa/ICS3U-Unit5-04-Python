#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: November 2019
# This program calculates the volume of a cylinder


import math


def calculate_volume(height, radius):
    # This function calculates the volume of the cylinder when called
    volume = round(math.pi*(radius ** 2) * height, 2)

    return volume


def main():
    print("Welcome to the cylinder volume calculator.")
    print("")
    height_from_user = input("Enter the height (cm): ")
    try:
        height_from_user = int(height_from_user)
        radius_from_user = input("Enter the radius (cm): ")
        try:
            radius_from_user = int(radius_from_user)
            calculated_volume = calculate_volume(height_from_user,
                                                 radius_from_user)
            print("")
            print("The volume of the cylinder is " + str(calculated_volume)
                  + "cm^3.")
        except Exception:
            print("Integers only. Try again.")
    except Exception:
        print("Integers only. Try again.")


if __name__ == "__main__":
    main()
