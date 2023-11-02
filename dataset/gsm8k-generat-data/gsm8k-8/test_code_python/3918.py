def solution():
    # Find the total number of pages in the book
    total_pages = sum([10, 15, 27, 12, 19]) / (1/3)

    # Find out how many pages Jesse has left to read
    pages_left = total_pages - sum([10, 15, 27, 12, 19])

    result = pages_left
    return result

print(solution())