def solution():
    """Sally sold 20 cups of lemonade last week. She sold 30% more lemonade this week. How many cups of lemonade did she sell in total for both weeks?"""
    # Define the number of cups sold last week
    cups_last_week = 20

    # Calculate the increase in sales this week
    increase = cups_last_week * 0.3

    # Calculate the total number of cups sold for both weeks
    total_cups = cups_last_week + increase

    result = total_cups
    return result

print(solution())