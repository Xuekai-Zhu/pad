def solution():
    """John decides to buy a month's supply of dog treats. He gives his dog 2 treats a day and they cost $.1 each. How much does he spend on the treats if the month is 30 days long?"""
    treats_per_day = 2
    cost_per_treat = 0.1
    days_in_month = 30
    total_treats = treats_per_day * days_in_month
    total_cost = total_treats * cost_per_treat
    result = total_cost
    return result

print(solution())