def solution():
    """Jack has a stack of books that is 12 inches thick. He knows from experience that 80 pages is one inch thick. If he has 6 books, how many pages is each one on average?"""
    stack_thickness = 12
    pages_per_inch = 80
    total_pages = stack_thickness * pages_per_inch
    num_books = 6
    pages_per_book = total_pages / num_books
    result = pages_per_book
    return result

print(solution())