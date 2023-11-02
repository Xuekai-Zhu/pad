def solution():
    """Maya loves to read books. Last week she read 5 books. Each book had 300 pages of text. This week she read twice as much. How many pages did Maya read in total?"""
    # Define the number of books Maya read last week and this week
    books_last_week = 5
    books_this_week = 10

    # Define the number of pages per book
    pages_per_book = 300

    # Calculate the total number of pages Maya read
    total_pages = (books_last_week + books_this_week) * pages_per_book

    # Display the total number of pages
    result = total_pages
    return result

print(solution())