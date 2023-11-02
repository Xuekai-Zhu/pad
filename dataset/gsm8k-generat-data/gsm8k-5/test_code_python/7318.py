def solution():
    pages_per_purple_book = 230  # Each purple book has 230 pages
    pages_per_orange_book = 510  # Each orange book has 510 pages
    purple_books_read = 5  # Mirella read 5 purple books
    orange_books_read = 4  # Mirella read 4 orange books

    # Calculate the total number of pages Mirella read from the purple books
    total_purple_pages = pages_per_purple_book * purple_books_read

    # Calculate the total number of pages Mirella read from the orange books
    total_orange_pages = pages_per_orange_book * orange_books_read

    # Calculate the difference between the total number of orange pages and purple pages
    diff = total_orange_pages - total_purple_pages
    result = diff
    return result

print(solution())