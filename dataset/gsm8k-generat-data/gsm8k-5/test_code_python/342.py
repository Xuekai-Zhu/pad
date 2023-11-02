def solution():
    total_game_time = 90  # The soccer game lasted for 90 minutes
    time_played_first = 20  # Mark played for 20 minutes at the start of the game
    time_played_second = 35  # Mark played for 35 minutes after his first rest

    # Calculate the total time Mark spent on the sideline
    time_on_sideline = total_game_time - time_played_first - time_played_second
    result = time_on_sideline
    return result

print(solution())