def solution():
    # Determine the total number of pages printed
    total_pages = 2 * 600

    # Determine the total number of sheets of paper used (assuming double-sided and 4 pages per side)
    total_sheets = total_pages / 4

    result = total_sheets
    return result

print(solution())