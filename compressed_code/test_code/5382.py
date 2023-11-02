def solution():
    
    chip_calories = 60 / 10
    cheezit_calories = chip_calories * (1 + 1/3)
    total_calories = 10 * chip_calories + 6 * cheezit_calories
    result = total_calories
    return result

print(solution())