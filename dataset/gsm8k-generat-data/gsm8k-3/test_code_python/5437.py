def solution():
    """Fred wants to order a variety pack of sliced meats for the upcoming game.  He can order a 4 pack of fancy, sliced meat for $40.00 and add rush delivery for an additional 30%.  With rush shipping added, how much will each type of sliced meat cost?"""
    # Define the cost of the pack of fancy, sliced meat
    original_cost = 40.00

    # Define the rush delivery fee
    rush_fee = original_cost * 0.3

    # Calculate the total cost with rush delivery
    total_cost = original_cost + rush_fee

    # Calculate the cost per slice of meat
    cost_per_slice = total_cost / 16

    # Display the cost per slice of meat
    result = cost_per_slice
    return result

print(solution())