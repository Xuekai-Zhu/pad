def solution():
    """Jackie's favorite cosmetic company was offering free shipping when you spent $50.00.
    Jackie ordered her favorite shampoo and conditioner that each cost $10.00 a bottle and 3 bottles of lotion
    that cost $6.00 each. How much more money does Jackie need to spend to be eligible for free shipping?"""
    # Define the prices of the shampoo, conditioner, and lotion
    shampoo_price = 10
    conditioner_price = 10
    lotion_price = 6

    # Calculate the total cost of the items Jackie purchased
    total_cost = (shampoo_price * 2) + (lotion_price * 3)

    # Calculate how much more money Jackie needs to spend to be eligible for free shipping
    remaining_cost = 50 - total_cost

    result = remaining_cost
    return result

print(solution())