def solution():
    """Dakota and Ben order eggs for $3, pancakes for $2, and 2 mugs of cocoa for $2 each. The tax is $1. Later, Ben then decides to order 1 more batch of pancakes and 1 more mug of cocoa as he is still hungry. How much change should they get from $15?"""
    # Define the prices of each item
    egg_price = 3
    pancake_price = 2
    cocoa_price = 2
    tax = 1

    # Calculate the total cost of the initial order
    total_cost = egg_price + (pancake_price*2) + (cocoa_price*2) + tax

    # Calculate the cost of the additional order
    additional_cost = pancake_price + cocoa_price

    # Calculate the total cost including the additional order
    new_total_cost = total_cost + additional_cost

    # Calculate the change from $15
    change = 15 - new_total_cost

    result = change
    return result

print(solution())