def solution():
    candy bars_per_week = 2
    weeks_between_eating = 4
    weeks_saved = 16
    total_candy_bars = candy_bars_per_week * weeks_saved
    candy_bars_eaten = weeks_between_eating * 4
    candy_bars_saved = total_candy_bars - candy_bars_eaten
    result = candy_bars_saved

print(solution())