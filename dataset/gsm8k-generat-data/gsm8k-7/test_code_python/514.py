def solution():
    total_stickers = 100
    stickers_given_to_boy = 10

    # Calculate the number of stickers left after giving some to the boy
    stickers_left = total_stickers - stickers_given_to_boy

    # Calculate the number of stickers to give to her best friends
    stickers_to_friends = stickers_left / 2

    # Calculate the number of stickers left after giving some to her best friends
    stickers_left = stickers_left - stickers_to_friends
    result = stickers_left
    return result

print(solution())