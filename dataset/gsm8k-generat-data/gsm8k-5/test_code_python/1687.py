def solution():
    max_load = 900  # The maximum load that a truck can carry
    bag_weight = 8  # The weight of one bag of lemons
    num_bags = 100  # The total number of bags of lemons

    # Calculate the total weight of the bags of lemons
    total_weight = bag_weight * num_bags

    # Calculate the remaining weight that can still be loaded into the truck
    remaining_weight = max_load - total_weight
    result = remaining_weight
    return result

print(solution())