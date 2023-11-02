def solution():
    # Calculate the total number of sheets of paper used by James
    total_pages = 2 * 600  # James prints out two 600-page books
    sheets_per_book = total_pages / 4  # each sheet has 4 pages (printed double-sided)
    total_sheets = sheets_per_book * 2  # James prints out two books
    result = total_sheets
    return result

print(solution())