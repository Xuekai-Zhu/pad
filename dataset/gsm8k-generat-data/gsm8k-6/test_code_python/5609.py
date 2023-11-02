def solution():
    # Calculate the total number of hours John has played in 2 weeks
    total_hours_played = 4 * 7 * 2  # 4 hours/day * 7 days/week * 2 weeks = 56 hours

    # Calculate the total hours of the game
    total_game_hours = total_hours_played / 0.4  # John is 40% done, so total_game_hours = total_hours_played / 0.4

    # Calculate the remaining hours of the game after increasing playtime to 7 hours/day
    remaining_game_hours = total_game_hours - total_hours_played
    days_to_finish_game = remaining_game_hours / 7  # assuming 7 hours of playtime per day

    result = days_to_finish_game
    return result

print(solution())