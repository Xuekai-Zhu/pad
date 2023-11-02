def solution():
    """James prints out 2 books. They are each 600 pages long. He prints out double-sided and 4 pages per side. How many sheets of paper does he use?"""
    pages_per_book = 600
    pages_per_sheet = 4
    sheets_per_book = pages_per_book / 2 / pages_per_sheet
    total_sheets = 2 * sheets_per_book
    result = total_sheets
    return result

print(solution())