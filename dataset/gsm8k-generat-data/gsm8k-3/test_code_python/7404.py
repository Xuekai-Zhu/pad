def solution():
    """Tom charges a fee of $100 a day to search for an item for the first 5 days and then $60 per day for every day after that.  How much did it cost for him to look for an item for 10 days?"""
    # Define the daily rates
    FIRST_FIVE_DAYS_RATE = 100
    AFTER_FIVE_DAYS_RATE = 60

    # Define the number of days Tom searched for the item
    number_of_days = 10

    # Calculate the cost for the first five days
    first_five_days_cost = FIRST_FIVE_DAYS_RATE * min(number_of_days, 5)

    # Calculate the cost for the remaining days
    remaining_days = max(0, number_of_days - 5)
    remaining_days_cost = AFTER_FIVE_DAYS_RATE * remaining_days

    # Calculate the total cost
    total_cost = first_five_days_cost + remaining_days_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())