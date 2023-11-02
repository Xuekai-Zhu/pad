def solution():
    """The cost of transporting 80 bags of cement, each weighing 50 kgs, is $6000. What's the cost of transporting three times as many cement bags, each weighing 3/5 times as many kgs?"""
    # Define the initial parameters
    initial_bags = 80
    initial_weight = 50
    initial_cost = 6000

    # Define the new parameters
    new_bags = 3 * initial_bags
    new_weight = 3/5 * initial_weight

    # Calculate the new cost based on the proportion of weight
    weight_proportion = new_weight / initial_weight
    new_cost = initial_cost * weight_proportion

    # Calculate the cost per bag and the final cost
    cost_per_bag = new_cost / new_bags
    final_cost = cost_per_bag * initial_bags

    # Return the result
    result = final_cost
    return result

print(solution())