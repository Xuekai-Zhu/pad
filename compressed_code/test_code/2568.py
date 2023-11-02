def solution():
    
    total_pages = 500
    written_pages_1 = 150
    remaining_pages_1 = total_pages - written_pages_1
    written_pages_2 = 0.3 * remaining_pages_1
    remaining_pages_2 = remaining_pages_1 - written_pages_2
    damaged_pages = 0.2 * remaining_pages_2
    empty_pages = remaining_pages_2 - damaged_pages
    result = empty_pages
    return result

print(solution())