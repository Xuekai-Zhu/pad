def solution():
    num_books = 2  # James is printing out 2 books
    pages_per_book = 600  # Each book is 600 pages long
    num_pages_per_sheet = 4  # James is printing double-sided with 4 pages per side

    # Calculate the total number of sheets of paper James uses
    num_sheets = (num_books * pages_per_book) // num_pages_per_sheet

    result = num_sheets
    return result

print(solution())