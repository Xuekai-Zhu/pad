def solution():
    
    runs = 40
    stairs_per_run = 32 * 2  
    calories_per_stair = 2
    total_calories = runs * stairs_per_run * calories_per_stair
    result = total_calories
    return result

print(solution())