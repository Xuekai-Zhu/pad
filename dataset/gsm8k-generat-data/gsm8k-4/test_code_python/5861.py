def solution():
    """Ralph has $54.00 worth of products in his cart. At the register, he asks if he could have a 20% discount on an item with a small issue. This item is $20.00 to start. They agree. Ralph also has a 10% coupon on his purchase, which he uses after the 20% discount on the item with the small issue. How much will all of his items cost?"""
    # Define the initial cost of Ralph's items in his cart
    initial_cost = 54.0

    # Define the cost of the item with the small issue
    item_cost = 20.0

    # Calculate the cost of the item with the 20% discount
    item_discounted_cost = item_cost - (item_cost * 0.2)

    # Calculate the cost of all of Ralph's items with the 20% discount applied to the item with the small issue
    total_cost = initial_cost - item_cost + item_discounted_cost

    # Calculate the cost of all of Ralph's items with the additional 10% coupon applied
    total_cost_with_coupon = total_cost - (total_cost * 0.1)

    # Return the final cost
    result = total_cost_with_coupon
    return result

print(solution())