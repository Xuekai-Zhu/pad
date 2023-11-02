def solution():
    
    initial_stickers = 100
    stickers_given = 10
    stickers_left = initial_stickers - stickers_given
    stickers_to_friends = stickers_left / 2
    total_stickers_left = stickers_left - stickers_to_friends
    result = total_stickers_left
    return result

print(solution())