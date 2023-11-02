def solution():
    # Define the weights of the apples and oranges
    apple_weight = 4
    orange_weight = 3

    # Calculate the total weight of each bag
    bag_weight = 49

    # Calculate the number of fruits in each bag
    fruits_per_bag = bag_weight // (apple_weight + orange_weight)

    # Calculate the number of apples needed for 3 full bags
    apples_per_bag = fruits_per_bag // 2
    total_apples = apples_per_bag * 3

    # Calculate the total weight of the apples needed
    total_apple_weight = total_apples * apple_weight
    result = total_apple_weight
    return result

print(solution())