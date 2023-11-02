def solution():
    
    page_goal = 140
    initial_pages_per_day = 3 * 6
    initial_total_pages = initial_pages_per_day * 7
    remaining_pages = page_goal - initial_total_pages
    additional_pages_per_day = remaining_pages / 7
    result = additional_pages_per_day
    return result

print(solution())