def solution():
    """Tom eats a pound of carrots and twice as much broccoli. If carrots have 51 calories per pound and broccoli has 1/3 that many calories, how many calories did he eat in total?"""
    # Define the number of pounds of carrots and broccoli
    carrots = 1
    broccoli = 2

    # Define the calorie count per pound of carrots and broccoli
    carrots_calories = 51
    broccoli_calories = 1/3 * carrots_calories

    # Calculate the total number of calories eaten
    total_calories = carrots * carrots_calories + broccoli * broccoli_calories

    result = total_calories
    return result

print(solution())