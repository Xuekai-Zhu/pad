def solution():
    """The football coach makes his players run up and down the bleachers 40 times. Each time they run up and down 32 stairs one way. If each stair burns 2 calories, how many calories does each player burn during this exercise?"""
    # Define the number of times the players run up and down the bleachers
    runs = 40

    # Define the number of stairs in one direction
    stairs = 32

    # Calculate the total number of stairs covered in one run
    total_stairs = stairs * 2

    # Calculate the total number of stairs covered in all runs
    total_stairs_all_runs = total_stairs * runs

    # Calculate the total number of calories burned
    calories_burned = total_stairs_all_runs * 2

    # Calculate the number of calories burned per player
    players = 1
    calories_per_player = calories_burned / players

    # return the result
    result = calories_per_player
    return result

print(solution())