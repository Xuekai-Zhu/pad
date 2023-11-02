def solution():
    # Define the initial number of stickers
    total_stickers = 135

    # Calculate the number of stickers Oliver used
    used_stickers = total_stickers * 1/3

    # Calculate the number of stickers he had remaining
    remaining_stickers = total_stickers - used_stickers

    # Calculate the number of stickers he gave to his friend
    friend_stickers = remaining_stickers * 2/5

    # Calculate the number of stickers he kept
    kept_stickers = remaining_stickers - friend_stickers
    result = kept_stickers
    return result

print(solution())