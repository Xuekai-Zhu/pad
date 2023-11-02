def solution():
    """Tom charges a fee of $100 a day to search for an item for the first 5 days and then $60 per day for every day after that. How much did it cost for him to look for an item for 10 days?"""
    first_five_days = 5
    remaining_days = 10 - first_five_days
    cost_first_five_days = 100 * first_five_days
    cost_remaining_days = 60 * remaining_days
    total_cost = cost_first_five_days + cost_remaining_days
    result = total_cost
    return result

print(solution())