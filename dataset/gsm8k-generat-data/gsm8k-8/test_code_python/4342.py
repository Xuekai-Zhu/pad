def solution():
    # Calculate the total number of stickers without losing any pages
    total_stickers = 20 * 12

    # Calculate the number of stickers on one page
    stickers_per_page = total_stickers / 12

    # Subtract the number of stickers on the lost page from the total number of stickers
    remaining_stickers = total_stickers - stickers_per_page

    result = remaining_stickers
    return result

print(solution())