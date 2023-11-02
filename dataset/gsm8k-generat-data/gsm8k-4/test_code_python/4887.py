def solution():
    """Oliver had 135 stickers. He used 1/3 of his stickers, gave 2/5 of the remaining to his friend, and kept the remaining stickers. How many stickers did he keep?"""
    # Define the initial number of stickers
    initial_stickers = 135

    # Calculate the number of stickers Oliver used
    used_stickers = initial_stickers / 3

    # Calculate the number of stickers Oliver had left
    remaining_stickers = initial_stickers - used_stickers

    # Calculate the number of stickers Oliver gave to his friend
    friend_stickers = remaining_stickers * 2 / 5

    # Calculate the number of stickers Oliver kept
    kept_stickers = remaining_stickers - friend_stickers

    # return the result
    result = kept_stickers
    return result

print(solution())