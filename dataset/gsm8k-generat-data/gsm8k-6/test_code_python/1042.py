def solution():
    candy_bars_per_week = 2
    candy_bars_eaten_per_month = 1/4
    weeks_saved = 16
    candy_bars_saved = (candy_bars_per_week - candy_bars_eaten_per_month) * weeks_saved
    result = candy_bars_saved
    return result

print(solution())