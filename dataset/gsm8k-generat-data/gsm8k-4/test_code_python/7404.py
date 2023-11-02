def solution():
    """Tom charges a fee of $100 a day to search for an item for the first 5 days and then $60 per day for every day after that. How much did it cost for him to look for an item for 10 days?"""
    # Define the daily fees for the first 5 days and after
    first_5_days_fee = 100
    after_5_days_fee = 60

    # Define the total number of days for the search
    total_days = 10

    # Calculate the fee for the first 5 days
    first_5_days_cost = first_5_days_fee * 5

    # Calculate the fee for the remaining days
    after_5_days_cost = (total_days - 5) * after_5_days_fee

    # Calculate the total cost
    total_cost = first_5_days_cost + after_5_days_cost

    # return the result
    result = total_cost
    return result

print(solution())