def solution():
    """Thomas buys a weight vest. It weighed 60 pounds and worked well for him in the beginning but after a bit of training he decides he wants to increase the weight by 60%. The weights come in 2-pound steel ingots. Each ingot cost $5 and if you buy more than 10 you get a 20% discount. How much does it cost to get the weight he needs?"""
    # Define the initial weight and the desired percentage increase in weight
    initial_weight = 60
    percent_increase = 60

    # Calculate the new weight and the weight increase
    new_weight = initial_weight + initial_weight * percent_increase / 100
    weight_increase = new_weight - initial_weight

    # Calculate the number of ingots needed
    ingots_needed = weight_increase / 2

    # Calculate the total cost of the ingots
    if ingots_needed > 10:
        cost_per_ingot = 5 * 0.8
    else:
        cost_per_ingot = 5
    total_cost = cost_per_ingot * ingots_needed

    # Return the result
    result = total_cost
    return result

print(solution())