def solution():
    total_thickness = 12
    pages_per_inch = 80
    num_books = 6

    # Calculate the total number of inches needed for all books
    total_book_thickness = total_thickness / num_books

    # Calculate the total number of pages for all books
    total_pages = total_book_thickness * pages_per_inch

    # Calculate the average number of pages per book
    avg_pages = total_pages / num_books
    result = avg_pages
    return result

print(solution())