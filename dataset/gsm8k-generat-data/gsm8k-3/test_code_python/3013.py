def solution():
    """John is lifting weights. He bench presses 15 pounds for 10 reps and does 3 sets. How much total weight does he move?"""
    # Define the weight and reps for each set
    WEIGHT = 15
    REPS = 10

    # Define the number of sets
    SETS = 3

    # Calculate the total weight moved
    total_weight = WEIGHT * REPS * SETS

    # Display the total weight
    result = total_weight
    return result

print(solution())