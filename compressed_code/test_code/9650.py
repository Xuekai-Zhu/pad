def solution():
    
    servings = 4
    cream_added = 0.5 
    fat_per_cup = 88 
    fat_per_serving = (cream_added * fat_per_cup) / servings
    result = fat_per_serving
    return result

print(solution())