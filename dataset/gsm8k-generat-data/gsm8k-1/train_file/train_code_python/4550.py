def solution():
    """Maria's birthday is in 22 days. Her friend Lilly wants to buy her flowers so she saves $2 each day until Maria's birthday. If a flower costs $4, how many flowers can she buy?"""
    days_to_save = 22
    savings_per_day = 2
    flower_cost = 4
    total_savings = days_to_save * savings_per_day
    flowers_can_buy = total_savings // flower_cost
    result = flowers_can_buy
    return result

print(solution())