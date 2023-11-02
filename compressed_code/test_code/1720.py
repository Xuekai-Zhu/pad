def solution():
    
    num_runs = 40
    num_stairs_per_run = 32 * 2   
    calories_burned_per_stair = 2
    total_stairs = num_runs * num_stairs_per_run
    total_calories_burned = total_stairs * calories_burned_per_stair
    result = total_calories_burned
    return result

print(solution())