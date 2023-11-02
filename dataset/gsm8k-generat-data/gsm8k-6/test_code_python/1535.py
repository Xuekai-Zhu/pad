def solution():
    # Calculate the total number of books Janine read in two months
    total_books = 5 + 2*5  # Janine read 5 books last month and twice as many this month
    pages_per_book = 10  # each book has 10 pages
    total_pages = total_books * pages_per_book  # calculate the total number of pages
    result = total_pages
    return result

print(solution())