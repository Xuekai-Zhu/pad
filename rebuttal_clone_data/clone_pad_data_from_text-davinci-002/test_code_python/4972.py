def solution():
    original_candy_bars = 7
    candy_bars_given = 3
    new_candy_bars = 30
    candy_bars_given_second_time = new_candy_bars / 4
    total_candy_bars_given = candy_bars_given + candy_bars_given_second_time
    candy_bars_kept = new_candy_bars + original_candy_bars - total_candy_bars_given
    result = candy_bars_kept
    return result

print(solution())