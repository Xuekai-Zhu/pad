def solution():
    """On Mary's birthday, her brother surprised her with $100. She spent a quarter of it on a new video game and then used a fifth of what was left on swimming goggles. How much money did she have left?"""
    # Define the initial amount of money
    initial_money = 100

    # Calculate the amount of money spent on the video game
    video_game_cost = initial_money * 0.25

    # Calculate the amount of money remaining after buying the video game
    remaining_money = initial_money - video_game_cost

    # Calculate the amount of money spent on swimming goggles
    goggles_cost = remaining_money * 0.2

    # Calculate the amount of money remaining after buying the swimming goggles
    final_money = remaining_money - goggles_cost

    # return the result
    result = final_money
    return result

print(solution())