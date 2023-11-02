def solution():
    # Calculate the number of people who watched the first game
    second_game_viewers = 80
    first_game_viewers = second_game_viewers - 20

    # Calculate the number of people who watched the third game
    third_game_viewers = second_game_viewers + 15

    # Calculate the total number of viewers for all three games
    total_viewers = first_game_viewers + second_game_viewers + third_game_viewers

    # Calculate the difference between the total viewers this week and last week
    difference = total_viewers - 200
    result = difference
    return result

print(solution())