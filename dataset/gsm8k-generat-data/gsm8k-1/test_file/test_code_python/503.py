def solution():
    """Janet takes two bus trips five days a week. If each bus trip costs her $2.20, how much would she save by buying a weekly bus pass for $20?"""
    daily_cost = 2.20 * 2
    weekly_cost = daily_cost * 5
    pass_cost = 20
    savings = weekly_cost - pass_cost
    result = savings
    return result

print(solution())