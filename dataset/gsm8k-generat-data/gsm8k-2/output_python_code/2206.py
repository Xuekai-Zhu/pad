def solution():
    """The football coach makes his players run up and down the bleachers 40 times. Each time they run up and down 32 stairs one way. If each stair burns 2 calories, how many calories does each player burn during this exercise?"""
    num_runs = 40
    num_stairs_per_run = 32 * 2   # up and down
    calories_burned_per_stair = 2
    total_stairs = num_runs * num_stairs_per_run
    total_calories_burned = total_stairs * calories_burned_per_stair
    result = total_calories_burned
    return result

print(solution())