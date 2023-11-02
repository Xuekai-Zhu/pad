def solution():
    six_day_war_duration = 6 * 24 * 60  # Convert 6 days to minutes
    nba_game_duration = (4 * 12 + 15) * 60  # Convert NBA game duration to minutes
    if nba_game_duration <= six_day_war_duration:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())