def solution():
    dolphin_stickers = 72  # Colton started with 72 dolphin stickers
    friends = 3  # Colton gave stickers to 3 friends
    stickers_per_friend = 4  # Colton gave each friend 4 stickers
    mandy_stickers = friends * stickers_per_friend + 2  # Mandy got 2 more than the total number of stickers given to friends
    justin_stickers = mandy_stickers - 10  # Justin got 10 less than Mandy

    # Calculate the total number of stickers given away
    total_given = friends * stickers_per_friend + mandy_stickers + justin_stickers

    # Calculate the number of stickers Colton has left
    left_over = dolphin_stickers - total_given
    result = left_over
    return result

print(solution())