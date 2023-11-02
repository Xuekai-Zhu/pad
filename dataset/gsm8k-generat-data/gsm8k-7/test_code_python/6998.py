def solution():
    book_pages = 210
    current_page = 90
    previous_page = 60

    # Calculate the number of pages read in the past hour
    pages_read = current_page - previous_page

    # Calculate the number of pages left to read in the book
    pages_left = book_pages - current_page

    # Calculate the total number of hours needed to finish the book
    hours_needed = pages_left / pages_read

    result = hours_needed
    return result

print(solution())