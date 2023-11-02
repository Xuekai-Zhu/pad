def solution():
    # Calculate the number of stickers Oliver kept
    stickers_used = 135 * (1/3)  # Oliver used 1/3 of his stickers
    stickers_remaining = 135 - stickers_used  # Calculate the number of stickers remaining
    stickers_given_away = stickers_remaining * (2/5)  # Oliver gave 2/5 of the remaining stickers to his friend
    stickers_kept = stickers_remaining - stickers_given_away  # Calculate the number of stickers Oliver kept
    result = stickers_kept
    return result

print(solution())