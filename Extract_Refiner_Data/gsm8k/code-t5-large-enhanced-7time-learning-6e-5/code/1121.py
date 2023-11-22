def solution():
    
    # Define the weight of each large bag and the total weight of M&M
    LARGE_BAG_WEIGHT = 10
    TOTAL_SMALL_BAG_WEIGHT = 30

    # Calculate the total weight of M&M in all the large bags
    total_large_bag_weight = LARGE_BAG_WEIGHT * 3

    # Calculate the total weight of M&M in all the small bags
    total_small_bag_weight = TOTAL_SMALL_BAG_WEIGHT * 3

    # Calculate the number of small bags that can be made with the remaining weight
    num_small_bags = total_small_bag_weight // LARGE_BAG_WEIGHT

    # Display the number of small bags that can be made
    result = num_small_bags
    return result

print(solution())