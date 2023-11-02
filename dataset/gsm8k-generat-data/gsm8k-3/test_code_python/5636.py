def solution():
    """Dakota and Ben order eggs for $3, pancakes for $2, and 2 mugs of cocoa for $2 each. The tax is $1. Later, Ben then decides to order 1 more batch of pancakes and 1 more mug of cocoa as he is still hungry. How much change should they get from $15?"""
    # Define the cost of each item
    EGG_PRICE = 3
    PANCAKE_PRICE = 2
    COCOA_PRICE = 2
    TAX = 1

    # Calculate the total cost of the initial order
    total_cost = EGG_PRICE + (PANCAKE_PRICE * 2) + (COCOA_PRICE * 2) + TAX

    # Calculate the total cost of the second order
    additional_pancakes = 1
    additional_cocoa = 1
    additional_cost = (additional_pancakes * PANCAKE_PRICE) + (additional_cocoa * COCOA_PRICE)

    # Calculate the total cost of both orders
    total_cost += additional_cost

    # Calculate the change from $15
    change = 15 - total_cost

    # Display the change
    result = change
    return result

print(solution())