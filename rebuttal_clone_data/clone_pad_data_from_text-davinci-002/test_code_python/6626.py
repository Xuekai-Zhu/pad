def solution():
    pages_per_book = 600
    pages_printed_per_side = 4
    sides_printed_per_sheet = 2
    sheets_used = pages_per_book / (pages_printed_per_side * sides_printed_per_sheet)
    result = sheets_used
    return result

print(solution())