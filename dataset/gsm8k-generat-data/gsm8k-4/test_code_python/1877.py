def solution():
    """Maya loves to read books. Last week she read 5 books. Each book had 300 pages of text. This week she read twice as much. How many pages did Maya read in total?"""
    # Define the number of books read last week and the number of pages per book
    BOOKS_LAST_WEEK = 5
    PAGES_PER_BOOK = 300

    # Calculate the total number of pages read last week
    pages_last_week = BOOKS_LAST_WEEK * PAGES_PER_BOOK

    # Calculate the number of books read this week and the total number of pages read this week
    books_this_week = BOOKS_LAST_WEEK * 2
    pages_this_week = books_this_week * PAGES_PER_BOOK

    # Calculate the total number of pages read
    total_pages = pages_last_week + pages_this_week

    # Return the result
    result = total_pages
    return result

print(solution())