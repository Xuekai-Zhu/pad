def solution():
    num_times_run = 40
    num_stairs = 32
    calories_burned_per_stair = 2

    # Calculate the total number of stairs run
    total_stairs_run = num_stairs * 2 * num_times_run

    # Calculate the total number of calories burned
    total_calories_burned = total_stairs_run * calories_burned_per_stair
    result = total_calories_burned
    return result

print(solution())