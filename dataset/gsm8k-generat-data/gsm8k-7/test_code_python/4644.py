def solution():
    total_water_used = 33
    roman_gallons = x
    remy_gallons = 3*x + 1

    # Set up equation to solve for x (number of gallons Roman used)
    # and then use that to calculate how many gallons Remy used
    x = (total_water_used - 1) / 4
    remy_gallons = 3*x + 1

    result = remy_gallons
    return result

print(solution())