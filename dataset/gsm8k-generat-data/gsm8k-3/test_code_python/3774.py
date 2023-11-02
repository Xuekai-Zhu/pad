def solution():
    """Oliver has two bags of vegetables. Each bag weighs 1/6 as much as James’s bag, which weighs 18kg. What is the combined weight of both Oliver’s bags?"""
    # Calculate the weight of each of Oliver's bags
    each_bag_weight = (1/6) * 18

    # Calculate the combined weight of both bags
    combined_weight = 2 * each_bag_weight

    # Display the combined weight of both bags
    result = combined_weight
    return result

print(solution())