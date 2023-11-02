def solution():
    """Jack has a stack of books that is 12 inches thick. He knows from experience that 80 pages is one inch thick. If he has 6 books, how many pages is each one on average?"""
    # Define the thickness of the stack of books in inches and the number of books
    stack_thickness = 12
    num_books = 6

    # Calculate the total number of pages in the stack of books
    total_pages = stack_thickness * 80

    # Calculate the average number of pages per book
    avg_pages_per_book = total_pages / num_books

    # Return the result
    result = avg_pages_per_book
    return result

print(solution())