def solution():
    # Define the weight of the empty lorry
    empty_weight = 500

    # Define the weight of each bag of apples
    bag_weight = 60

    # Define the number of bags of apples
    num_bags = 20

    # Calculate the weight of the loaded lorry
    loaded_weight = empty_weight + (num_bags * bag_weight)

    result = loaded_weight
    return result

print(solution())