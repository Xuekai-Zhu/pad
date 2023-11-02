def solution():
    """Before Marcus went on a road trip to LA, his car had 1728 miles on it. He filled his empty gas tank twice and used up all the gas on the trip. If Marcus's car gets 30 miles per gallon and holds 20 gallons of gas, how many miles does Marcus' car have on it now?"""
    starting_mileage = 1728
    gallons_per_fill = 20
    mpg = 30
    total_miles_driven = 0
    for i in range(2):
        total_miles_driven += gallons_per_fill * mpg

    final_mileage = starting_mileage + total_miles_driven
    result = final_mileage
    return result

print(solution())