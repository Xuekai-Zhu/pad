def solution():
    """There are 20 stickers on a page. If you have 12 pages of stickers but lose one of the pages, then how many stickers would you have?"""
    stickers_per_page = 20
    pages = 12
    lost_pages = 1
    remaining_pages = pages - lost_pages
    total_stickers = remaining_pages * stickers_per_page
    result = total_stickers
    return result

print(solution())