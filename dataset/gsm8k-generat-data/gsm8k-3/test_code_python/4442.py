def solution():
    """Thomas buys a weight vest.  It weighed 60 pounds and worked well for him in the beginning but after a bit of training he decides he wants to increase the weight by 60%.  The weights come in 2-pound steel ingots.  Each ingot cost $5 and if you buy more than 10 you get a 20% discount.  How much does it cost to get the weight he needs?"""
    # Define the initial weight of the vest
    initial_weight = 60

    # Calculate the new weight of the vest after a 60% increase
    new_weight = initial_weight * 1.6

    # Calculate the number of 2-pound steel ingots needed to reach the new weight
    ingots_needed = new_weight / 2

    # Calculate the cost of buying the required number of ingots
    if ingots_needed <= 10:
        total_cost = ingots_needed * 5
    else:
        # Apply the 20% discount for buying more than 10 ingots
        cost_per_ingot = 5 * 0.8
        total_cost = ingots_needed * cost_per_ingot

    # Display the total cost
    result = total_cost
    return result

print(solution())