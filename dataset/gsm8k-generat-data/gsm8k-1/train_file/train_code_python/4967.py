def solution():
    """Tom eats a pound of carrots and twice as much broccoli. If carrots have 51 calories per pound and broccoli has 1/3 that many calories, how many calories did he eat in total?"""
    carrots = 1
    broccoli = 2
    carrot_calories = 51
    broccoli_calories_per_pound = carrot_calories / 3
    total_carrot_calories = carrots * carrot_calories
    total_broccoli_calories = broccoli * broccoli_calories_per_pound
    total_calories = total_carrot_calories + total_broccoli_calories
    result = total_calories
    return result

print(solution())