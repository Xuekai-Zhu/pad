def solution():
    """Jon drinks a bottle of water that is 16 ounces every 4 hours for the 16 hours he is awake.  Twice a day he also drinks a bottle that is 25% larger than those bottles.  How much fluid does he drink a week?"""
    # Define the size of Jon's regular water bottles
    REGULAR_SIZE = 16

    # Define the number of regular water bottles Jon drinks in a day
    regular_bottles_per_day = 16 / 4

    # Define the size of Jon's larger water bottles
    LARGER_SIZE = REGULAR_SIZE * 1.25

    # Define the number of larger water bottles Jon drinks in a day
    larger_bottles_per_day = 2

    # Calculate the total fluid Jon drinks in a day
    daily_fluid = (regular_bottles_per_day * REGULAR_SIZE) + (larger_bottles_per_day * LARGER_SIZE)

    # Calculate the total fluid Jon drinks in a week
    weekly_fluid = daily_fluid * 7

    # Display the total fluid Jon drinks in a week
    result = weekly_fluid
    return result

print(solution())