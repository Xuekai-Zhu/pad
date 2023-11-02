def solution():
    total_game_time = 90
    mark_played_time1 = 20
    mark_played_time2 = 35

    # Calculate the total time Mark was on the sideline
    sideline_time = total_game_time - mark_played_time1 - mark_played_time2
    result = sideline_time
    return result

print(solution())