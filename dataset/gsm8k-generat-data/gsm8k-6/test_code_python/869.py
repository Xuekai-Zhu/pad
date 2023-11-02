def solution():
    # Calculate the total number of stickers Paige has
    total_stickers = 100 + 50  # a sheet of 100 space stickers and a sheet of 50 cat stickers
    stickers_per_friend = total_stickers // 3  # divide the stickers equally among her 3 friends
    left_over_stickers = total_stickers - stickers_per_friend * 3  # calculate the stickers Paige has left over
    result = left_over_stickers
    return result

print(solution())