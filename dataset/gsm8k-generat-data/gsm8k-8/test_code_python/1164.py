def solution():
    # Define the starting amount of water
    starting_water = 40

    # Calculate the amount of water lost in the first two hours
    lost_water_2_hours = 2 * 2

    # Calculate the amount of water at the end of hour two
    water_after_2_hours = starting_water - lost_water_2_hours

    # Add 1 gallon of water in hour three
    water_after_3_hours = water_after_2_hours + 1

    # Add 3 gallons of water in hour four
    water_after_4_hours = water_after_3_hours + 3

    result = water_after_4_hours
    return result

print(solution())