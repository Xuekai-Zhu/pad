def solution():
    bottle_pack = 24
    first_day = bottle_pack / 3
    left_bottles = bottle_pack - first_day
    second_day = left_bottles / 2
    total_bottles_left = left_bottles - second_day
    result = total_bottles_left
    return result

print(solution())