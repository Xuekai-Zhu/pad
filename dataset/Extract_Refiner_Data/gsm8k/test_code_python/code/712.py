def solution():
    
    # Define the number of ounces of cheese and the number of calories per ounce for each egg omelet
    CHEESE_OUNCES = 2
    CHEESE_CALORIES = 120
    HAM_OUNCES = 1
    HAM_CALORIES = 40

    # Define the number of egg omelets
    num_omelets = 6

    # Calculate the total number of calories for each egg omelet
    egg_calories = 75 * num_omelets
    cheese_calories = CHEESE_OUNCES * CHEESE_CALORIES
    ham_calories = HAM_OUNCES * HAM_CALORIES

    # Calculate the total number of calories for all omelets
    total_calories = egg_calories + cheese_calories + ham_calories

    # Display the total number of calories
    result = total_calories
    return result

print(solution())