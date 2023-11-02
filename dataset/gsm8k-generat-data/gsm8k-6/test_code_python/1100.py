def solution():
    # Calculate the total number of stickers used
    total_used = 3 + 7*6  # 3 large stickers on front page and 7 stickers on 6 other pages

    # Calculate the number of stickers remaining
    remaining_stickers = 89 - total_used
    result = remaining_stickers
    return result

print(solution())