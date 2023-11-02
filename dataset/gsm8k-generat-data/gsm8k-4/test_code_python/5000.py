def solution():
    """Ray buys a pack of hamburger meat for $5.00, a box of crackers for $3.50, 4 bags of frozen vegetables at $2.00 per bag and a pack of cheese for $3.50 at the grocery store.  Because he is a store rewards member, he gets 10% off of his purchase.  What does his total grocery bill come to?"""
    # Define the prices of the items
    hamburger_price = 5.00
    crackers_price = 3.50
    vegetables_price = 2.00
    cheese_price = 3.50

    # Calculate the total cost of the items
    total_cost = hamburger_price + crackers_price + 4 * vegetables_price + cheese_price

    # Calculate the discount amount
    discount_amount = total_cost * 0.1

    # Calculate the total cost after the discount
    discounted_cost = total_cost - discount_amount

    # Round the total cost to two decimal places
    result = round(discounted_cost, 2)
    return result

print(solution())