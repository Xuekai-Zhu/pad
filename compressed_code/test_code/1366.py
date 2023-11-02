def solution():
    
    goal_pages = 800
    book1_pages = 500
    book1_progress = 0.8
    book2_pages = 1000
    book2_progress = 1/5

    total_read = book1_pages * book1_progress + book2_pages * book2_progress
    remaining_pages = goal_pages - total_read
    result = remaining_pages
    return result

print(solution())