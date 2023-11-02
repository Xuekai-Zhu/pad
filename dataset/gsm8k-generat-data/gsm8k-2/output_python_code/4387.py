def solution():
    """A classroom of 15 students turned in essays on Friday morning. The first 5 students each turned in essays with 2 pages. The next 5 students each turned in essays with 3 pages. The last 5 students each turned in essays with 1 page. What is the average page count per essay for the 15 students?"""
    pages_1 = 2
    pages_2 = 3
    pages_3 = 1
    count_1 = 5
    count_2 = 5
    count_3 = 5
    total_pages = (pages_1 * count_1) + (pages_2 * count_2) + (pages_3 * count_3)
    average_page_count = total_pages / 15
    result = average_page_count
    return result

print(solution())