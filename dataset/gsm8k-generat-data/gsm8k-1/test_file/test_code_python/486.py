def solution():
    """
    An 8-year old child wants to buy a toy car which costs $12. He already has $4 savings. How many days will it take him to save the remaining amount of money if he promises to save $2 daily from his allowance?
    """
    total_cost = 12
    savings = 4
    daily_savings = 2
    remaining_cost = total_cost - savings
    days_to_save = remaining_cost / daily_savings
    result = days_to_save
    return result

print(solution())