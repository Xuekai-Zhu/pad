def solution():
    
    total_pages = 500
    pages_written_1st_week = 150
    remaining_pages = total_pages - pages_written_1st_week
    pages_written_2nd_week = 0.3 * remaining_pages
    remaining_pages -= pages_written_2nd_week
    damaged_pages = 0.2 * remaining_pages
    empty_pages = remaining_pages - damaged_pages
    result = empty_pages
    return result

print(solution())