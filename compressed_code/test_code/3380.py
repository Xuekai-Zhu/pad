def solution():
    
    stickers_per_page = 20
    total_pages = 12
    lost_page = 1
    remaining_pages = total_pages - lost_page
    total_stickers = remaining_pages * stickers_per_page
    result = total_stickers
    return result

print(solution())