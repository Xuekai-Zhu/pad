def solution():
    """Brenda bakes 20 cakes a day. She does this for 9 days and then sells half of the cakes. How many cakes are left with Brenda?"""
    cakes_per_day = 20
    days_baking = 9
    total_cakes = cakes_per_day * days_baking
    cakes_sold = total_cakes / 2
    cakes_left = total_cakes - cakes_sold
    result = cakes_left
    return result

print(solution())