def solution():
    num_stickers = 89
    num_large_stickers = 3
    num_small_stickers_per_page = 7
    num_pages = 6

    # Calculate the total number of small stickers used
    num_small_stickers_used = num_small_stickers_per_page * num_pages

    # Calculate the total number of stickers used
    num_stickers_used = num_large_stickers + num_small_stickers_used

    # Calculate the number of stickers remaining
    num_stickers_remaining = num_stickers - num_stickers_used
    result = num_stickers_remaining
    return result

print(solution())