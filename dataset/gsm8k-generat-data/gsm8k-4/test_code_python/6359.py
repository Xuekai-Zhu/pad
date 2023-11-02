def solution():
    """Parker went to the gym and found 4 twenty pounds dumbbells set up for weightlifting. He added two more dumbbells to the setup and started his exercises. How many pounds of dumbbells is Parker using for his exercises?"""
    # Define the weight of each dumbbell in pounds
    DUMBBELL_WEIGHT = 20

    # Define the initial number of dumbbells
    initial_dumbbells = 4

    # Define the number of additional dumbbells
    additional_dumbbells = 2

    # Calculate the total weight of the dumbbells in pounds
    total_weight = (initial_dumbbells + additional_dumbbells) * DUMBBELL_WEIGHT

    # return the result
    result = total_weight
    return result

print(solution())