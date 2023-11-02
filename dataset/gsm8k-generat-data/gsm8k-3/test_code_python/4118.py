def solution():
    """Jessica is making an apple pie. She knows that each serving requires 1.5 apples and she has 12 guests. She plans to make 3 pies, which each contain 8 servings. If her guests finish all the pie, on average, how many apples does each guest eat?"""
    # Define the number of apples per serving and the number of pies
    APPLES_PER_SERVING = 1.5
    NUM_PIES = 3

    # Calculate the total number of servings and the total number of apples
    total_servings = 8 * NUM_PIES
    total_apples = total_servings * APPLES_PER_SERVING

    # Calculate the average number of apples per guest
    avg_apples_per_guest = total_apples / 12

    # Display the average number of apples per guest
    result = avg_apples_per_guest
    return result

print(solution())