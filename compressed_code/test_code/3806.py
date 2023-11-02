def solution():
    
    servings = 4
    cream_cup = 0.5
    fat_per_cup = 88
    total_fat = cream_cup * fat_per_cup
    fat_per_serving = total_fat / servings
    result = fat_per_serving
    return result

print(solution())