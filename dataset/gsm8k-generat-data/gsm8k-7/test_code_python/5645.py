def solution():
    num_bags1 = 12
    weight1 = 24
    num_bags2 = 8

    # Calculate the weight of one bag of oranges
    bag_weight = weight1 / num_bags1

    # Calculate the weight of 8 bags of oranges
    weight2 = num_bags2 * bag_weight
    result = weight2
    return result

print(solution())