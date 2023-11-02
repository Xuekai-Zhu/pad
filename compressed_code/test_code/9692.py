def solution():
    
    initial_candy_bars = 7
    candy_bars_given_initial = 3
    new_candy_bars = 30
    candy_bars_given_new = candy_bars_given_initial * 4
    total_given = candy_bars_given_initial + candy_bars_given_new
    total_candy_bars = initial_candy_bars + new_candy_bars
    candy_bars_kept = total_candy_bars - total_given
    result = candy_bars_kept
    return result

print(solution())