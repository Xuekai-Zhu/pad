def solution():
    # Define the number of books Maya read
    num_books = 5

    # Define the number of pages per book
    pages_per_book = 300

    # Calculate the total number of pages Maya read last week
    total_pages_last_week = num_books * pages_per_book

    # Calculate the total number of pages Maya read this week
    total_pages_this_week = 2 * total_pages_last_week

    # Calculate the total number of pages Maya read in total
    total_pages = total_pages_last_week + total_pages_this_week
    result = total_pages
    return result

print(solution())