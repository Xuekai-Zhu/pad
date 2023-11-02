def solution():
    """Jessica is making an apple pie. She knows that each serving requires 1.5 apples and she has 12 quests. She plans to make 3 pies, which each contain 8 servings. If her guests finish all the pie, on average , how many apples does each guest eat?"""
    # Calculate the total number of servings
    total_servings = 3 * 8

    # Calculate the total number of apples
    total_apples = total_servings * 1.5

    # Calculate the average number of apples per guest
    apples_per_guest = total_apples / 12

    # round the result to 1 decimal place
    result = round(apples_per_guest, 1)
    return result

print(solution())