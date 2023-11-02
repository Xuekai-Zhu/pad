def solution():
    """Trey is raising money for a new bike that costs $112. He plans to spend the next two weeks selling bracelets for $1 each. On average, how many bracelets does he need to sell each day?"""
    bike_cost = 112
    weeks = 2
    days = 7 * weeks
    total_bracelets_needed = bike_cost
    bracelets_per_day = total_bracelets_needed / days
    result = bracelets_per_day
    return result

print(solution())