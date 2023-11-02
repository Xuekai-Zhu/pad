def solution():
    num_bags = 80
    weight_per_bag = 50
    cost = 6000

    # Calculate the cost per kg of cement in the original transport
    cost_per_kg = cost / (num_bags * weight_per_bag)

    # Calculate the new number of bags and weight per bag
    new_num_bags = num_bags * 3
    new_weight_per_bag = weight_per_bag * (3/5)

    # Calculate the total weight of the new transport
    new_total_weight = new_num_bags * new_weight_per_bag

    # Calculate the cost of the new transport
    new_cost = new_total_weight * cost_per_kg
    result = new_cost
    return result

print(solution())