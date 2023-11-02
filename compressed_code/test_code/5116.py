def solution():
    
    pages_per_book = 600
    pages_per_sheet = 4
    sheets_per_book = pages_per_book / 2 / pages_per_sheet
    total_sheets = 2 * sheets_per_book
    result = total_sheets
    return result

print(solution())