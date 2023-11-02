def solution():
    
    initial_candy_bars = 7
    first_gift = 3
    bought_candy_bars = 30
    second_gift = 4 * first_gift
    remaining_candy_bars = initial_candy_bars + bought_candy_bars - first_gift - second_gift
    result = remaining_candy_bars
    return result

print(solution())