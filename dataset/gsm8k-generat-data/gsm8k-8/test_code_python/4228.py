def solution():
    daily_allowance = 12
    saved_per_day = 0.5 * daily_allowance
    total_saved_first_six_days = 6 * saved_per_day
    saved_on_seventh_day = 0.25 * saved_per_day
    total_saved = total_saved_first_six_days + saved_on_seventh_day
    result = total_saved
    return result

print(solution())