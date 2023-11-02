def solution():
    """Terry eats 2 yogurts a day. They are currently on sale at 4 yogurts for $5.00. How much does he spend on yogurt over 30 days?"""
    yogurt_per_day = 2
    yogurt_per_pack = 4
    cost_per_pack = 5.0
    days = 30
    packs_per_day = yogurt_per_day / yogurt_per_pack
    packs_per_month = packs_per_day * days
    cost_per_month = packs_per_month * cost_per_pack
    result = cost_per_month
    return result

print(solution())