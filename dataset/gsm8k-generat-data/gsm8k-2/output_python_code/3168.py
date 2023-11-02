def solution():
    """John cuts his grass to 2 inches. It grows .5 inches per month. When it gets to 4 inches he cuts it back down to 2 inches. It cost $100 to get his grass cut. How much does he pay per year?"""
    months_per_year = 12
    growth_per_month = 0.5
    height_before_cutting = 4
    height_after_cutting = 2

    months_between_cuttings = (height_before_cutting - height_after_cutting) / growth_per_month
    total_cuttings_per_year = months_per_year / months_between_cuttings
    cost_per_cutting = 100
    total_cost_per_year = total_cuttings_per_year * cost_per_cutting

    result = total_cost_per_year
    return result

print(solution())