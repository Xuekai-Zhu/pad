def solution():
    """Harper drinks a 1/2 bottle of mineral water per day. She buys the mineral water by the case at a big box store. They come 24 bottles to a case and are currently on sale for $12.00. If she wants to buy enough cases to last her 240 days, how much will she spend?"""
    daily_bottles = 0.5
    bottles_per_case = 24
    days = 240
    cases_needed = (daily_bottles * days) / bottles_per_case
    case_price = 12
    total_cost = cases_needed * case_price
    result = total_cost
    return result

print(solution())