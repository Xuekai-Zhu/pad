def solution():
    """Katherine has 5 hanging baskets to fill. In each basket, she wants to add 3 petunias and 2 sweet potato vines. The petunias cost $3.00 apiece and the sweet potato vines cost $2.50 apiece. How much will she spend filling all 5 hanging baskets?"""
    num_baskets = 5
    num_petunias_per_basket = 3
    cost_per_petunia = 3.00
    num_sweet_potato_per_basket = 2
    cost_per_sweet_potato = 2.50
    total_cost = (num_petunias_per_basket * cost_per_petunia + num_sweet_potato_per_basket * cost_per_sweet_potato) * num_baskets
    result = total_cost
    return result

print(solution())