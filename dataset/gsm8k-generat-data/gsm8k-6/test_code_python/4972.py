def solution():
    # Calculate the total number of candy bars Amanda kept for herself
    initial_candy_bars = 7
    candy_bars_given_first_time = 3
    candy_bars_given_second_time = candy_bars_given_first_time * 4  # Amanda gave her sister 4 times as many candy bars the second time
    candy_bars_bought = 30
    candy_bars_kept = initial_candy_bars + candy_bars_bought - candy_bars_given_first_time - candy_bars_given_second_time
    result = candy_bars_kept
    return result

print(solution())