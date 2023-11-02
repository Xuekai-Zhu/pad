def solution():
    """James prints out 2 books.  They are each 600 pages long.  He prints out double-sided and 4 pages per side.  How many sheets of paper does he use?"""
    # Define the number of pages in each book and the number of pages per sheet
    PAGES_PER_BOOK = 600
    PAGES_PER_SHEET = 4

    # Calculate the number of sheets used for each book
    sheets_per_book = PAGES_PER_BOOK / 2 / PAGES_PER_SHEET

    # Calculate the total number of sheets used for both books
    total_sheets = sheets_per_book * 2

    # Display the total number of sheets used
    result = total_sheets
    return result

print(solution())