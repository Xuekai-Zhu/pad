def solution():
    # Calculate the total number of stairs climbed by each player
    total_stairs = 40 * 32 * 2  # each time the players run up and down, they climb 32 stairs one way and then 32 stairs back down

    # Calculate the number of calories burned by each player
    calories_burned = total_stairs * 2  # each stair burns 2 calories

    result = calories_burned
    return result

print(solution())