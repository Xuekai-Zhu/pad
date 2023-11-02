def solution():
    """Rita bought 5 short dresses, 3 pairs of pants and 4 jackets from a store that sells second-hand clothes. The dresses cost $20 each, the pants cost $12, the jackets cost $30 each, and she spent an additional $5 on transportation. If she had $400 initially, how much does she have now?"""
    # Define the prices of each item
    DRESS_PRICE = 20
    PANTS_PRICE = 12
    JACKET_PRICE = 30

    # Define the quantity of each item purchased
    dress_qty = 5
    pants_qty = 3
    jacket_qty = 4

    # Calculate the total cost of dresses
    dress_cost = dress_qty * DRESS_PRICE

    # Calculate the total cost of pants
    pants_cost = pants_qty * PANTS_PRICE

    # Calculate the total cost of jackets
    jacket_cost = jacket_qty * JACKET_PRICE

    # Calculate the total cost of transportation
    transportation_cost = 5

    # Calculate the total cost of the purchase
    total_cost = dress_cost + pants_cost + jacket_cost + transportation_cost

    # Calculate the remaining amount of money
    remaining_money = 400 - total_cost

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())