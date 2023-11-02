def solution():
    """A retailer sells any shirt for the same price and any pair of pants for the same price, but the price of shirts and pants are not the same. Say you bought 2 shirts and 3 pairs of pants for $120 in total, then you realized you didn't need the extra pants. What's the price of 1 shirt at this place if when you returned all 3 pairs of pants you were refunded 25% of what you originally paid?"""
    # Define the initial total cost and the number of shirts and pants purchased
    total_cost = 120
    shirts = 2
    pants = 3

    # Calculate the cost of one pair of pants
    pants_cost = (total_cost / 5) - (shirts * (total_cost / 5) / (shirts + pants))

    # Calculate the cost of one shirt
    shirt_cost = (total_cost / 5) - pants_cost

    # Calculate the total refund received when returning the pants
    refund = pants_cost * pants * 0.25

    # Calculate the final cost of the shirts after the refund
    final_cost = total_cost - refund

    # Calculate the price of one shirt
    shirt_price = final_cost / shirts

    # return the result
    result = shirt_price
    return result

print(solution())