def solution():
    # Calculate the total number of stickers
    total_stickers = 20 * 12  # 20 stickers on each of 12 pages

    # Calculate the number of stickers after losing one page
    remaining_stickers = total_stickers - 20  # losing one page means losing 20 stickers
    result = remaining_stickers
    return result

print(solution())