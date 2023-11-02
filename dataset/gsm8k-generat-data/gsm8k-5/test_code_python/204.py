def solution():
    stack_thickness = 12  # The stack of books is 12 inches thick
    pages_per_inch = 80  # Jack knows that 80 pages is one inch thick
    num_books = 6  # Jack has 6 books in total

    # Calculate the total number of pages in the stack of books
    total_pages = stack_thickness * pages_per_inch

    # Calculate the average number of pages per book
    avg_pages_per_book = total_pages / num_books
    result = avg_pages_per_book
    return result

print(solution())