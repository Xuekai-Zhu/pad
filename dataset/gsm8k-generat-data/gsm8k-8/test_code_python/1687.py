def solution():
    # Define the weight of one bag of lemons and the maximum load of the truck
    bag_weight = 8
    max_load = 900

    # Calculate the total weight of 100 bags of lemons
    total_weight = bag_weight * 100

    # Calculate the remaining weight that can still be loaded into the truck
    remaining_weight = max_load - total_weight
    result = remaining_weight
    return result

print(solution())