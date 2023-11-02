def solution():
    """A classroom of 15 students turned in essays on Friday morning. The first 5 students each turned in essays with 2 pages. The next 5 students each turned in essays with 3 pages. The last 5 students each turned in essays with 1 page. What is the average page count per essay for the 15 students?"""
    first_5_essays = 5 * 2
    next_5_essays = 5 * 3
    last_5_essays = 5 * 1
    total_essays = 15
    total_pages = first_5_essays + next_5_essays + last_5_essays
    avg_page_count = total_pages / total_essays
    result = avg_page_count
    return result

print(solution())