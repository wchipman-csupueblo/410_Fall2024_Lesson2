#!/usr/bin/env python3

print("The Miles per Gallon program")
print()


another_trip = "y"

while another_trip == "y":


    miles_driven = float(input("Enter miles driven:          "))
    gallons_used = float(input("Enter gallons of gas used:        "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        mpg = round(miles_driven / gallons_used, 2)
        total_gas_cost = round(gallons_used * cost_per_gallon, 1)
        cost_per_mile = round(total_gas_cost/miles_driven, 1)
        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost Per Miles:            ", cost_per_mile)
        print()

    another_trip = input("Get entries for another trip (y/n)? ")
    print()

print("Bye!")
