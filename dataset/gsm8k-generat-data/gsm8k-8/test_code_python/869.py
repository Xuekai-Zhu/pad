def solution():
    # Calculate the total number of stickers Paige has
    total_stickers = 100 + 50

    # Divide the total number of stickers equally among the 3 friends
    stickers_per_friend = total_stickers / 3

    # Calculate the total number of stickers Paige gives away
    total_given_away = stickers_per_friend * 3

    # Calculate the number of stickers Paige has left
    stickers_left = total_stickers - total_given_away
    result = stickers_left
    return result

print(solution())