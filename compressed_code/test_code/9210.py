def solution():
    
    stickers_per_page = 20
    pages = 12
    lost_pages = 1
    remaining_pages = pages - lost_pages
    total_stickers = remaining_pages * stickers_per_page
    result = total_stickers
    return result

print(solution())