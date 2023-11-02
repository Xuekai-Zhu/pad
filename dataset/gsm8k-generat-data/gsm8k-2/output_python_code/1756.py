def solution():
    """Arthur knows that he needs to finish 800 pages of reading over the summer. He has read 80% of a 500-page book and 1/5 of a 1000 page book. How many more pages does he need to reach to meet his goal?"""
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