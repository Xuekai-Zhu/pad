def solution():
    # Define the initial amount of water
    initial_water = 24

    # Calculate the amount of water left after day 1
    left_after_day1 = initial_water - (1/3) * initial_water

    # Calculate the amount of water left after day 2
    left_after_day2 = left_after_day1 - (1/2) * left_after_day1

    result = left_after_day2
    return result

print(solution())