def solution():
    """Jack has a stack of books that is 12 inches thick. He knows from experience that 80 pages is one inch thick. If he has 6 books, how many pages is each one on average?"""
    thickness = 12
    pages_per_inch = 80
    num_books = 6
    total_pages = thickness * pages_per_inch
    avg_pages_per_book = total_pages / num_books
    result = avg_pages_per_book
    return result

print(solution())