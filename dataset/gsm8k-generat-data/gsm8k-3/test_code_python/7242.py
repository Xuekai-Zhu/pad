def solution():
    """John drinks 1.5 gallons of water a day.  How many quarts does he drink a week?"""
    # Define the number of gallons John drinks per day and the number of quarts in a gallon
    GALLONS_PER_DAY = 1.5
    QUARTS_PER_GALLON = 4

    # Calculate the number of quarts John drinks per week
    quarts_per_week = GALLONS_PER_DAY * 7 * QUARTS_PER_GALLON

    # Display the number of quarts John drinks per week
    result = quarts_per_week
    return result

print(solution())