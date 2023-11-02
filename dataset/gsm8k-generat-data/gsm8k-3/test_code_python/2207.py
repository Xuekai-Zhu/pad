def solution():
    """The football coach makes his players run up and down the bleachers 40 times. Each time they run up and down 32 stairs one way. If each stair burns 2 calories, how many calories does each player burn during this exercise?"""
    # Define the number of times the players run up and down the bleachers
    num_runs = 40

    # Define the number of stairs in each run
    num_stairs = 32 * 2

    # Define the number of calories burned per stair
    calories_per_stair = 2

    # Calculate the total number of stairs climbed
    total_stairs = num_runs * num_stairs

    # Calculate the total calories burned
    total_calories = total_stairs * calories_per_stair

    # Display the total calories burned
    result = total_calories
    return result

print(solution())