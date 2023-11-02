def solution():
    weekdays = 5  # Sally reads 10 pages on weekdays
    weekends = 2  # Sally reads 20 pages on weekends
    total_days = 14  # It takes 2 weeks for Sally to finish the book

    # Calculate the total number of pages Sally reads
    total_pages = (weekdays * 10 * 2) + (weekends * 20)

    # Calculate the number of pages in the book
    book_pages = total_pages / total_days
    result = book_pages
    return result

print(solution())