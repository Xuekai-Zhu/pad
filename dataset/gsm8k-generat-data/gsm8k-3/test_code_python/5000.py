def solution():
    """Ray buys a pack of hamburger meat for $5.00, a box of crackers for $3.50, 4 bags of frozen vegetables at $2.00 per bag and a pack of cheese for $3.50 at the grocery store.  Because he is a store rewards member, he gets 10% off of his purchase.  What does his total grocery bill come to?"""
    # Define the prices of each item
    hamburger_price = 5.00
    crackers_price = 3.50
    vegetables_price = 2.00
    cheese_price = 3.50

    # Calculate the total cost of each item
    hamburger_cost = hamburger_price
    crackers_cost = crackers_price
    vegetables_cost = 4 * vegetables_price
    cheese_cost = cheese_price

    # Calculate the subtotal of the purchase
    subtotal = hamburger_cost + crackers_cost + vegetables_cost + cheese_cost

    # Calculate the discount
    discount = 0.10 * subtotal

    # Calculate the total cost
    total_cost = subtotal - discount

    # Display the total cost
    result = total_cost
    return result

print(solution())