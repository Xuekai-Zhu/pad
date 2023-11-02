def solution():
    # Define the initial amount of money
    initial_money = 100

    # Calculate the amount spent on the video game
    video_game_cost = initial_money / 4

    # Calculate the amount of money left after buying the video game
    money_left = initial_money - video_game_cost

    # Calculate the amount spent on swimming goggles
    goggles_cost = money_left / 5

    # Calculate the final amount of money left
    final_money_left = money_left - goggles_cost
    result = final_money_left
    return result

print(solution())