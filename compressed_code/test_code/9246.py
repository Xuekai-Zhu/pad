def solution():
    
    first_5_essays = 5 * 2
    next_5_essays = 5 * 3
    last_5_essays = 5 * 1
    total_essays = 15
    total_pages = first_5_essays + next_5_essays + last_5_essays
    avg_page_count = total_pages / total_essays
    result = avg_page_count
    return result

print(solution())