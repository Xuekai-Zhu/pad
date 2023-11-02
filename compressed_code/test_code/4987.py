def solution():
    
    initial_bottles = 10
    lost_bottles = 2
    stolen_bottles = 1
    remaining_bottles = initial_bottles - lost_bottles - stolen_bottles
    stickers_per_bottle = 3
    total_stickers = remaining_bottles * stickers_per_bottle
    result = total_stickers
    return result

print(solution())