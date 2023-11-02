def solution():
    final_fantasy_vi_position = 6
    total_main_series_games = 15
    if final_fantasy_vi_position <= total_main_series_games/2:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())