def solution():
    """Roman and Remy took separate showers. Remy used 1 more gallon than 3 times the number of gallons that Roman used for his shower. Together the boys used 33 gallons of water. How many gallons did Remy use?"""
    # Define the amount of water used by Roman
    roman_water = None

    # Define the amount of water used by Remy
    remy_water = 3 * roman_water + 1

    # Define the total amount of water used by both boys
    total_water = 33

    # Solve the system of equations
    # roman_water + remy_water = total_water
    # remy_water = 3 * roman_water + 1
    roman_water = (total_water - 1) / 4
    remy_water = 3 * roman_water + 1

    result = remy_water
    return result

print(solution())