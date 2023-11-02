def solution():
    # Calculate the amount Mary spent on a new video game
    spent_on_video_game = 100/4

    # Calculate the amount of money left after buying the video game
    money_left = 100 - spent_on_video_game

    # Calculate the amount Mary spent on swimming goggles
    spent_on_goggles = money_left/5

    # Calculate the total amount of money Mary has left
    money_left = money_left - spent_on_goggles

    result = money_left
    return result

print(solution())