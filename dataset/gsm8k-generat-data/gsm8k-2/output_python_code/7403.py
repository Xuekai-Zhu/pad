def solution():
    """Tom charges a fee of $100 a day to search for an item for the first 5 days and then $60 per day for every day after that. How much did it cost for him to look for an item for 10 days?"""
    first_five_days_cost = 100 * 5
    remaining_days = 10 - 5
    after_five_days_cost = 60 * remaining_days
    total_cost = first_five_days_cost + after_five_days_cost
    result = total_cost
    return result

print(solution())