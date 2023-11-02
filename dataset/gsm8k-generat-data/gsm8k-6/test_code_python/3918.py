def solution():
    # Calculate the total number of pages in the book
    total_pages = sum([10, 15, 27, 12, 19]) * 3  # multiply by 3 to account for the fact that he only read 1/3 of the book
    remaining_pages = total_pages - sum([10, 15, 27, 12, 19])  # subtract the pages he already read
    result = remaining_pages
    return result

print(solution())