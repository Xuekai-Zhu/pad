def solution():
    """A store gives a 10% discount for the amount of the sell that was over $1000.  John buys 7 items that each cost $200.  What does his order cost after the discount?"""
    # Define the cost of each item and the number of items purchased
    ITEM_COST = 200
    NUM_ITEMS = 7

    # Calculate the total cost before the discount
    total_cost = ITEM_COST * NUM_ITEMS

    # Check if the total cost is over $1000
    if total_cost > 1000:
        # Calculate the amount of the discount
        discount_amount = (total_cost - 1000) * 0.1

        # Apply the discount to the total cost
        total_cost = total_cost - discount_amount

    # Display the total cost of the order
    result = total_cost
    return result

print(solution())