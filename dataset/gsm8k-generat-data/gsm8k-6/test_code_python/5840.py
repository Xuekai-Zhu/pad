def solution():
    # Calculate the total number of pages in Phil's books
    total_pages = 10 * 100  # 10 books with 100 pages each

    # Subtract the pages from the lost books
    remaining_pages = total_pages - (2 * 100)  # 2 books lost, each with 100 pages

    result = remaining_pages
    return result

print(solution())