def solution():
    initial_water_bottles = 10
    lost_bottles = 2
    stolen_bottles = 1
    remaining_bottles = initial_water_bottles - lost_bottles - stolen_bottles

    stickers_per_bottle = 3
    total_stickers_used = remaining_bottles * stickers_per_bottle
    result = total_stickers_used
    return result

print(solution())