def solution():
    # Calculate the total gallons of water needed for the first two tanks
    first_two_tanks = 8 + 8

    # Calculate the gallons of water needed for the last two tanks
    last_two_tanks = (8 - 2) + (8 - 2)

    # Calculate the total gallons of water needed for all four tanks
    total_gallons = first_two_tanks + last_two_tanks

    # Calculate the gallons of water needed for four weeks
    water_per_week = total_gallons * 4

    result = water_per_week
    return result

print(solution())