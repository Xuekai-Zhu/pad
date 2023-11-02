def solution():
    """John cuts his grass to 2 inches. It grows .5 inches per month. When it gets to 4 inches he cuts it back down to 2 inches. It cost $100 to get his grass cut. How much does he pay per year?"""
    desired_height = 2
    growth_per_month = 0.5
    growth_per_year = growth_per_month * 12
    time_until_cut = (4 - desired_height) / growth_per_month
    cuts_per_year = 12 / time_until_cut
    cost_per_cut = 100
    total_cost_per_year = cost_per_cut * cuts_per_year
    result = total_cost_per_year
    return result

print(solution())