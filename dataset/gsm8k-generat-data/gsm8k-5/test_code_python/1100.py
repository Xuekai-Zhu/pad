def solution():
    total_stickers = 89  # Mary has 89 stickers
    front_page_stickers = 3  # Mary used 3 stickers on the front page of her journal
    page_stickers = 7  # Mary used 7 stickers on each of the 6 other pages

    # Calculate the total number of stickers used
    used_stickers = front_page_stickers + (6 * page_stickers)

    # Calculate the number of stickers remaining
    remaining_stickers = total_stickers - used_stickers
    result = remaining_stickers
    return result

print(solution())