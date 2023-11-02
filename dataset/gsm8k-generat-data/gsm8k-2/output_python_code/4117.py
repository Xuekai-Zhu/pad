def solution():
    """Jessica is making an apple pie. She knows that each serving requires 1.5 apples and she has 12 quests. She plans to make 3 pies, which each contain 8 servings. If her guests finish all the pie, on average, how many apples does each guest eat?"""
    servings_per_pie = 8
    apples_per_serving = 1.5
    num_pies = 3
    num_guests = 12
    total_servings = servings_per_pie * num_pies
    total_apples = total_servings * apples_per_serving
    apples_per_guest = total_apples / num_guests
    result = round(apples_per_guest, 2)
    return result

print(solution())