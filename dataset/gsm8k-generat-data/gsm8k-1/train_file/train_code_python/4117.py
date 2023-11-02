def solution():
    """Jessica is making an apple pie. She knows that each serving requires 1.5 apples and she has 12 quests.
    She plans to make 3 pies, which each contain 8 servings. If her guests finish all the pie, on average, how many
    apples does each guest eat?"""
    servings_per_pie = 8
    pies = 3
    guests = 12
    apples_per_serving = 1.5
    total_apples = servings_per_pie * pies * apples_per_serving
    apples_per_guest = total_apples / guests
    result = apples_per_guest
    return result

print(solution())