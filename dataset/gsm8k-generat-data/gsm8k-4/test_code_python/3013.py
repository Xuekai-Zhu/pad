def solution():
    """John is lifting weights. He bench presses 15 pounds for 10 reps and does 3 sets. How much total weight does he move?"""
    # Define the weight John lifts per rep
    weight_per_rep = 15

    # Define the number of reps John does per set
    reps_per_set = 10

    # Define the number of sets John does
    num_sets = 3

    # Calculate the total weight John moves
    total_weight = weight_per_rep * reps_per_set * num_sets

    # Return the result
    result = total_weight
    return result

print(solution())