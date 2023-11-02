def solution():
    # Define the variables
    bags = 80
    weight = 50
    cost = 6000

    # Calculate the new weight per bag
    new_weight = weight * 3/5

    # Calculate the new number of bags
    new_bags = bags * 3

    # Calculate the new total weight
    new_total_weight = new_weight * new_bags

    # Calculate the cost per unit weight
    cost_per_unit_weight = cost / (bags * weight)

    # Calculate the new total cost
    new_total_cost = new_total_weight * cost_per_unit_weight

    result = new_total_cost
    return result

print(solution())