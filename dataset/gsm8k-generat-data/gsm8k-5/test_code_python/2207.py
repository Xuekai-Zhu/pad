def solution():
    num_runs = 40  # The players run up and down the bleachers 40 times
    stairs_per_run = 32 * 2  # The players run up and down 32 stairs one way, so 64 stairs per run
    calories_per_stair = 2  # Each stair burns 2 calories

    # Calculate the total number of stairs the players run up and down
    total_stairs = num_runs * stairs_per_run

    # Calculate the total number of calories burned by each player
    calories_burned = total_stairs * calories_per_stair
    result = calories_burned
    return result

print(solution())