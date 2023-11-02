def solution():
    """Amanda had 7 candy bars. She gave 3 to her sister. The next day, Amanda won some prize money and bought another 30 candy bars. She gave her sister 4 times as many candy bars as she did the first time. How many candy bars did Amanda keep for herself altogether?"""
    initial_candy_bars = 7
    first_gift = 3
    bought_candy_bars = 30
    second_gift = 4 * first_gift
    remaining_candy_bars = initial_candy_bars + bought_candy_bars - first_gift - second_gift
    result = remaining_candy_bars
    return result

print(solution())