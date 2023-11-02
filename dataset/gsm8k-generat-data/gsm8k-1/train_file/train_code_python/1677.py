def solution():
    """Jackie's favorite cosmetic company was offering free shipping when you spent $50.00. Jackie ordered her favorite shampoo and conditioner that each cost $10.00 a bottle and 3 bottles of lotion that cost $6.00 each. How much more money does Jackie need to spend to be eligible for free shipping?"""
    shampoo_cost = 10
    conditioner_cost = 10
    lotion_cost = 6
    num_lotions = 3
    total_cost = (shampoo_cost * 2) + (lotion_cost * num_lotions)
    amount_needed_for_shipping = 50 - total_cost
    result = amount_needed_for_shipping
    return result

print(solution())