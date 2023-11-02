def solution():
    
    initial_stickers = 72
    stickers_given = 4 * 3
    mandy_given = stickers_given + 2
    justin_given = mandy_given - 10
    total_given = stickers_given + mandy_given + justin_given
    stickers_left = initial_stickers - total_given
    result = stickers_left
    return result

print(solution())