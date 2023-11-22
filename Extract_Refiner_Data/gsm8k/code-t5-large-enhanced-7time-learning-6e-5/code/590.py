def solution():
    
    # Define the weight of a cup of mushrooms and protein
    MUSHROOM_WEIGHT = 100
    POTOR_WEIGHT = 3

    # Define the amount of mushrooms John eats every day
    MUSHROOMS_PER_DAY = 200

    # Calculate the total weight of mushrooms John eats every day
    total_weight_per_day = MUSHROOM_WEIGHT * MUSHROOMS_PER_DAY

    # Calculate the total weight of protein John eats every day
    total_weight_per_week = total_weight_per_day * 7

    # Calculate the amount of protein John gets per week
    protein_per_week = total_weight_per_week - total_weight_per_day

    # Display the amount of protein John gets per week
    result = protein_per_week
    return result

print(solution())