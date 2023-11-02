def solution():
    num_large_bags = 3
    weight_per_bag = 10
    ounces_per_bag = 30

    # Calculate the total weight of all large bags
    total_weight = num_large_bags * weight_per_bag

    # Calculate the number of small bags that can be made
    num_small_bags = total_weight // weight_per_bag
    result = num_small_bags
    return result

print(solution())