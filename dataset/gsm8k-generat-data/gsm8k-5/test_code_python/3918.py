def solution():
    # Calculate the total number of pages in the book
    total_pages = (5 / (1/3)) * sum([10, 15, 27, 12, 19])

    # Calculate the number of pages Jesse still needs to read
    pages_remaining = total_pages - sum([10, 15, 27, 12, 19])

    result = pages_remaining
    return result

print(solution())