def solution():
    """Every day Tom drinks 5 12-oz cans of soda plus 64 ounces of water. How many ounces of fluid does he drink a week?"""
    # Define the number of cans of soda Tom drinks and the amount of water he drinks per day
    SODA_PER_DAY = 5
    SODA_SIZE = 12 # in ounces
    WATER_PER_DAY = 64

    # Calculate the total amount of fluid Tom drinks per day
    fluid_per_day = SODA_PER_DAY * SODA_SIZE + WATER_PER_DAY

    # Calculate the total amount of fluid Tom drinks per week
    fluid_per_week = fluid_per_day * 7

    result = fluid_per_week
    return result

print(solution())