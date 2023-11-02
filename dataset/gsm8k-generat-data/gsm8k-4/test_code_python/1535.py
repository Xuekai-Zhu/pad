def solution():
    """Janine read 5 books last month. This month, she read twice as many books. If each book has 10 pages, how many pages did Janine read in two months?"""
    # Calculate the total number of books read over two months
    total_books = 5 + 2 * 5

    # Calculate the total number of pages read
    total_pages = total_books * 10

    # Return the result
    result = total_pages
    return result

print(solution())