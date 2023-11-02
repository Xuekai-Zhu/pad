def solution():
    """A lorry is 500 pounds when empty. What will its weight be if it's loaded with 20 bags of apples, each weighing 60 pounds?"""
    # Define the weight of an empty lorry and the weight of each bag of apples
    empty_weight = 500
    apple_bag_weight = 60

    # Calculate the total weight of the bags of apples
    total_apple_weight = apple_bag_weight * 20

    # Calculate the weight of the loaded lorry
    loaded_weight = empty_weight + total_apple_weight

    # Return the result
    result = loaded_weight
    return result

print(solution())