def solution():
    """Mr. Alvarez spends $36 on diesel fuel each week. If the cost of diesel fuel is $3 per gallon, how many gallons of diesel fuel does Mr. Alvarez use in two weeks?"""
    # Define the cost of diesel fuel per gallon and the cost per week
    DIESEL_PRICE_PER_GALLON = 3
    WEEKLY_COST = 36

    # Calculate the number of gallons used in one week
    gallons_per_week = WEEKLY_COST / DIESEL_PRICE_PER_GALLON

    # Calculate the number of gallons used in two weeks
    gallons_per_two_weeks = gallons_per_week * 2

    result = gallons_per_two_weeks
    return result

print(solution())