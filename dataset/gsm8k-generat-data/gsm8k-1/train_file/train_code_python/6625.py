def solution():
    """James prints out 2 books. They are each 600 pages long. He prints out double-sided and 4 pages per side. How many sheets of paper does he use?"""
    num_books = 2
    num_pages = 600
    num_sides = 2
    pages_per_side = 4
    total_pages = num_books * num_pages
    total_sheets = (total_pages / num_sides) / pages_per_side
    result = total_sheets
    return result

print(solution())