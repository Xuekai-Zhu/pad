def solution():
    """Shiela is required to submit a 15-page research paper. She already finished writing 1/3 of the paper. How many pages does she have left to write?"""
    total_pages = 15
    completed_pages = total_pages * (1/3)
    pages_left = total_pages - completed_pages
    result = pages_left
    return result

print(solution())