def solution():
    # Define the initial number of stickers
    initial_stickers = 72

    # Calculate the total number of stickers given to the three friends
    friend_stickers = 4 * 3

    # Calculate the number of stickers given to Mandy
    mandy_stickers = friend_stickers + 2

    # Calculate the number of stickers given to Justin
    justin_stickers = mandy_stickers - 10

    # Calculate the total number of stickers given away
    total_given_away = friend_stickers + mandy_stickers + justin_stickers

    # Calculate the number of stickers remaining
    stickers_remaining = initial_stickers - total_given_away
    result = stickers_remaining
    return result

print(solution())