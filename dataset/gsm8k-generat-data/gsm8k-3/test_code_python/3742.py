def solution():
    """A retailer sells any shirt for the same price and any pair of pants for the same price, but the price of shirts and pants are not the same. Say you bought 2 shirts and 3 pairs of pants for $120 in total, then you realized you didn't need the extra pants. What's the price of 1 shirt at this place if when you returned all 3 pairs of pants you were refunded 25% of what you originally paid?"""
    # Define the number of shirts and pants purchased
    shirts = 2
    pants = 3

    # Define the initial cost and the cost after the pants were returned
    initial_cost = 120
    returned_cost = initial_cost * 0.75

    # Calculate the total cost of the shirts
    shirt_cost = returned_cost - (pants * (returned_cost / (shirts + pants)))

    # Calculate the price of each shirt
    price_per_shirt = shirt_cost / shirts

    # Display the price of each shirt
    result = price_per_shirt
    return result

print(solution())