def solution():
    # Define the number of shirts and pants purchased
    shirts = 2
    pants = 3

    # Define the total cost of the purchase
    total_cost = 120

    # Calculate the cost of one pair of pants
    pants_cost = (total_cost / (shirts + pants)) * pants

    # Calculate the cost of one shirt
    shirt_cost = (total_cost - (pants_cost * pants)) / shirts

    # Calculate the refund amount when the pants are returned
    refund_amount = 0.25 * (total_cost - (shirt_cost * shirts))

    # Calculate the final cost of the shirts
    final_cost = total_cost - (refund_amount + (pants_cost * pants))

    # Calculate the price of one shirt
    price_of_one_shirt = final_cost / shirts

    result = price_of_one_shirt
    return result

print(solution())