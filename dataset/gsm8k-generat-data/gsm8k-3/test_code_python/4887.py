def solution():
    """Oliver had 135 stickers. He used 1/3 of his stickers, gave 2/5 of the remaining stickers to his friend, and kept the rest. How many stickers did he keep?"""
    # Define the total number of stickers
    total_stickers = 135

    # Calculate the number of stickers Oliver used
    used_stickers = total_stickers // 3

    # Calculate the number of stickers Oliver had left
    remaining_stickers = total_stickers - used_stickers

    # Calculate the number of stickers Oliver gave to his friend
    friend_stickers = remaining_stickers * 2 // 5

    # Calculate the number of stickers Oliver had left after giving some to his friend
    kept_stickers = remaining_stickers - friend_stickers

    # Display the number of stickers Oliver kept
    result = kept_stickers
    return result

print(solution())