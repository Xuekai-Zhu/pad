def solution():
    """Chastity bought 4 lollipops which cost $1.50 each, and she also bought 2 packs of gummies which cost $2 each. If she has $15, how much was she left with after spending on the candies?"""
    lollipops_cost = 1.5
    gummies_cost = 2
    num_lollipops = 4
    num_gummies = 2
    total_cost = (lollipops_cost * num_lollipops) + (gummies_cost * num_gummies)
    amount_left = 15 - total_cost
    result = amount_left
    return result

print(solution())