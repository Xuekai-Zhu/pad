def solution():
    num_books = 2
    pages_per_book = 600
    pages_per_side = 4
    
    # Calculate the total number of sheets of paper used for one book
    sheets_per_book = pages_per_book / pages_per_side / 2
    
    # Calculate the total number of sheets of paper used for both books
    total_sheets = sheets_per_book * num_books
    result = total_sheets
    return result

print(solution())