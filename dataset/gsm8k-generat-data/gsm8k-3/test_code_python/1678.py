def solution():
    """Jackie's favorite cosmetic company was offering free shipping when you spent $50.00.  Jackie ordered her favorite shampoo and conditioner that each cost $10.00 a bottle and 3 bottles of lotion that cost $6.00 each.  How much more money does Jackie need to spend to be eligible for free shipping?"""
    # Define the prices of each product
    SHAMPOO_PRICE = 10
    CONDITIONER_PRICE = 10
    LOTION_PRICE = 6

    # Define the quantities purchased by Jackie
    shampoo_qty = 1
    conditioner_qty = 1
    lotion_qty = 3

    # Calculate the total cost of the items purchased
    total_cost = (shampoo_qty * SHAMPOO_PRICE) + (conditioner_qty * CONDITIONER_PRICE) + (lotion_qty * LOTION_PRICE)

    # Calculate the amount Jackie needs to spend for free shipping
    free_shipping_threshold = 50
    amount_needed = free_shipping_threshold - total_cost

    # Display the amount needed for free shipping
    result = amount_needed
    return result

print(solution())