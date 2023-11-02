def solution():
    """On Mary's birthday, her brother surprised her with $100. She spent a quarter of it on a new video game and then used a fifth of what was left on swimming goggles. How much money did she have left?"""
    # Define the initial amount of money Mary received
    initial_amount = 100

    # Calculate the amount Mary spent on the new video game
    video_game_cost = initial_amount / 4

    # Calculate the amount Mary had left after buying the video game
    remaining_amount = initial_amount - video_game_cost

    # Calculate the amount Mary spent on swimming goggles
    goggles_cost = remaining_amount / 5

    # Calculate the amount Mary had left after buying the goggles
    final_amount = remaining_amount - goggles_cost

    # Display the final amount Mary had left
    result = final_amount
    return result

print(solution())