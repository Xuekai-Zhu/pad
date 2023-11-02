def solution():
    """Tom eats a pound of carrots and twice as much broccoli. If carrots have 51 calories per pound and broccoli has 1/3 that many calories, how many calories did he eat in total?"""
    carrot_weight = 1
    broccoli_weight = 2
    carrot_calories = 51
    broccoli_calories = 1/3 * carrot_calories
    total_calories = carrot_weight * carrot_calories + broccoli_weight * broccoli_calories
    result = total_calories
    return result

print(solution())