def solution():
    num_stickers = 72
    num_friends = 3
    stickers_per_friend = 4
    mandy_stickers = num_friends * stickers_per_friend + 2
    justin_stickers = mandy_stickers - 10

    # Calculate the total number of stickers given away
    total_given = (num_friends * stickers_per_friend) + mandy_stickers + justin_stickers

    # Calculate the number of stickers remaining
    num_remaining = num_stickers - total_given
    result = num_remaining
    return result

print(solution())