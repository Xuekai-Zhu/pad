def solution():
    """Nate is reading a 400-page book. He finished reading 20% of the book. How many pages does he need to read to finish the book?"""
    total_pages = 400
    percent_finished = 20
    pages_finished = total_pages * (percent_finished / 100)
    pages_left = total_pages - pages_finished
    result = pages_left
    return result

print(solution())