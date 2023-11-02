def solution():
    """James prints out 2 books. They are each 600 pages long. He prints out double-sided and 4 pages per side. How many sheets of paper does he use?"""
    # Define the number of pages per book and the number of sides per sheet
    PAGES_PER_BOOK = 600
    SIDES_PER_SHEET = 2

    # Calculate the total number of sheets needed for both books
    total_sheets = (PAGES_PER_BOOK * 2) / (SIDES_PER_SHEET * 4)

    # Return the result
    result = total_sheets
    return result

print(solution())