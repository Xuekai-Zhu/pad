def solution():
    starting_bags = 55  # The trader starts with 55 bags of rice
    restocked_bags = 132  # The trader restocks 132 bags of rice
    ending_bags = 164  # The trader ends with 164 bags of rice

    # Calculate the number of bags the trader sold
    sold_bags = starting_bags + restocked_bags - ending_bags
    result = sold_bags
    return result

print(solution())