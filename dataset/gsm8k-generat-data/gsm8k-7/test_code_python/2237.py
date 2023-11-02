def solution():
    initial_money = 100

    # Calculate the amount spent on the video game
    video_game_price = initial_money * 0.25

    # Calculate the amount of money left after buying the video game
    remaining_money = initial_money - video_game_price

    # Calculate the amount spent on swimming goggles
    goggles_price = remaining_money * 0.2

    # Calculate the amount of money left after buying the swimming goggles
    money_left = remaining_money - goggles_price
    result = money_left
    return result

print(solution())