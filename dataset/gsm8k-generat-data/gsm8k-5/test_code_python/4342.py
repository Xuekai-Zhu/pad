def solution():
    stickers_per_page = 20  # There are 20 stickers on a page
    pages_with_lost_page = 12 - 1  # There are 12 pages initially, but one page is lost
    total_stickers = stickers_per_page * pages_with_lost_page  # Calculate the total number of stickers

    result = total_stickers
    return result

print(solution())