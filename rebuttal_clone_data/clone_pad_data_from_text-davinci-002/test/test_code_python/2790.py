def solution():
    cream_per_cup = 88
    cream_added = 0.5
    total_cream = cream_per_cup * cream_added
    servings = 4
    fat_per_serving = total_cream / servings
    result = fat_per_serving
    return result

print(solution())