def solution():
    """Jack has a stack of books that is 12 inches thick. He knows from experience that 80 pages is one inch thick. If he has 6 books, how many pages is each one on average?"""
    # Define the thickness of the stack of books and the number of books
    BOOK_STACK_THICKNESS = 12  # inches
    NUM_BOOKS = 6

    # Define the number of pages per inch
    PAGES_PER_INCH = 80

    # Calculate the total number of pages in the stack of books
    total_pages = BOOK_STACK_THICKNESS * PAGES_PER_INCH

    # Calculate the average number of pages per book
    avg_pages_per_book = total_pages / NUM_BOOKS

    # Return the result
    result = avg_pages_per_book
    return result

print(solution())