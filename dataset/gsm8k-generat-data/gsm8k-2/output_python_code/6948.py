def solution():
    """
    John eats 10 potato chips that have a total of 60 calories. He then eats 6 cheezits that each have 1/3 more calories
    than a chip. How many total calories did he eat?
    """
    chip_calories = 60 / 10
    cheezit_calories = chip_calories * (1 + 1/3)
    total_calories = 10 * chip_calories + 6 * cheezit_calories
    result = total_calories
    return result

print(solution())