def solution():
    # Define the number of stickers Clara brings to school
    initial_stickers = 100

    # Subtract the number of stickers given to the boy she likes
    stickers_left = initial_stickers - 10

    # Calculate how many stickers Clara gives to her best friends
    stickers_given = stickers_left / 2

    # Subtract the number of stickers given to her best friends
    stickers_left = stickers_left - stickers_given
    result = stickers_left
    return result

print(solution())