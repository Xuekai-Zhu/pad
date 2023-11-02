def solution():
    """Cilia wants to buy a multi-level dumbbell system.  The first pair of dumbbells are 3 lb weights, the second pair is 5 lb weights and the third is 8 lb pounds.  How much does the entire system weigh?"""
    # Define the weight of each pair of dumbbells
    WEIGHTS = [3, 5, 8]

    # Calculate the total weight of the dumbbell system
    total_weight = sum(WEIGHTS) * 2

    # Display the total weight
    result = total_weight
    return result

print(solution())