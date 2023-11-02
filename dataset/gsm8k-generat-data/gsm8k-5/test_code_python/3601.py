def solution():
    # Calculate the total gallons of water needed for the first two tanks
    first_two_tanks = 8 * 2

    # Calculate the gallons of water needed for the other two tanks
    other_tanks = (8 - 2) * 2  # Two gallons less than the first two tanks

    # Calculate the total gallons of water needed for all four tanks
    total_gallons = first_two_tanks + other_tanks

    # Calculate the total gallons of water needed in four weeks
    total_gallons_in_four_weeks = total_gallons * 4
    result = total_gallons_in_four_weeks
    return result

print(solution())