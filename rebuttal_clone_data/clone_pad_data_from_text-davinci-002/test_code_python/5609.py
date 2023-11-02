def solution():
    days_in_two_weeks = 14
    hours_played_so_far = days_in_two_weeks * 4
    game_completion_percentage = 40
    hours_needed_to_complete = hours_played_so_far / (game_completion_percentage / 100)
    hours_played_per_day = 7
    days_needed_to_complete = hours_needed_to_complete / hours_played_per_day
    result = days_needed_to_complete
    return result

print(solution())