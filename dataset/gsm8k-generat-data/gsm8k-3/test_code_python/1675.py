def solution():
    """A lorry is 500 pounds when empty. What will its weight be if it's loaded with 20 bags of apples, each weighing 60 pounds?"""
    # Define the weight of an empty lorry and the weight of each bag of apples
    EMPTY_WEIGHT = 500
    BAG_WEIGHT = 60

    # Calculate the total weight of the loaded lorry
    total_weight = EMPTY_WEIGHT + (20 * BAG_WEIGHT)

    # Display the total weight
    result = total_weight
    return result

print(solution())