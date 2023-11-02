def solution():
    """Jackie's favorite cosmetic company was offering free shipping when you spent $50.00. Jackie ordered her favorite shampoo and conditioner that each cost $10.00 a bottle and 3 bottles of lotion that cost $6.00 each. How much more money does Jackie need to spend to be eligible for free shipping?"""
    shampoo_cost = 10
    conditioner_cost = 10
    lotion_cost = 6
    total_cost = (shampoo_cost * 2) + (lotion_cost * 3)
    needed_cost_for_free_shipping = 50
    difference = needed_cost_for_free_shipping - total_cost
    result = difference
    return result

print(solution())