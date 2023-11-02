def solution():
    """Harper drinks a 1/2 bottle of mineral water per day. She buys the mineral water by the case at a big box store. They come 24 bottles to a case and are currently on sale for $12.00. If she wants to buy enough cases to last her 240 days, how much will she spend?"""
    bottles_per_day = 0.5
    bottles_per_case = 24
    days_in_case = bottles_per_case / bottles_per_day
    cases_needed = 240 / days_in_case
    case_price = 12.00
    total_price = cases_needed * case_price
    result = total_price
    
    return result

print(solution())