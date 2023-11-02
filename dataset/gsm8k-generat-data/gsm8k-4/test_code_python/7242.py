def solution():
    """John drinks 1.5 gallons of water a day. How many quarts does he drink a week?"""
    # Define the number of gallons consumed per day
    gallons_per_day = 1.5

    # Calculate the number of quarts consumed per day
    quarts_per_day = gallons_per_day * 4

    # Calculate the number of quarts consumed per week
    quarts_per_week = quarts_per_day * 7

    # Return the result
    result = quarts_per_week
    return result

print(solution())