def solution():
    # Calculate the amount of carbon dioxide released per shopping trip using plastic bags
    plastic_carbon = 8 * 4 / 16 # in pounds

    # Calculate the number of shopping trips needed to equal the carbon output of the canvas bag
    trips_needed = 600 / plastic_carbon

    result = round(trips_needed)
    return result

print(solution())