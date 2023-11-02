def solution():
    num_games_played = 200 + 100
    num_games_won = int(0.63 * 200) + (100 - 43)

    # Calculate the new win percentage
    win_percentage = (num_games_won / num_games_played) * 100
    result = win_percentage
    return result

print(solution())