def solution():
    """Every day Tom drinks 5 12-oz cans of soda plus 64 ounces of water. How many ounces of fluid does he drink a week?"""
    # Define the amount of fluid Tom drinks each day
    SODA_OUNCES = 12 * 5
    WATER_OUNCES = 64
    TOTAL_OUNCES = SODA_OUNCES + WATER_OUNCES

    # Calculate the amount of fluid Tom drinks in a week
    WEEKLY_OUNCES = TOTAL_OUNCES * 7

    # Display the result
    result = WEEKLY_OUNCES
    return result

print(solution())