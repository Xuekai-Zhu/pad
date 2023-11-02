def solution():
    """Janine read 5 books last month. This month, she read twice as many books. If each book has 10 pages, how many pages did Janine read in two months?"""
    # Define the number of books read last month and this month
    last_month_books = 5
    this_month_books = last_month_books * 2

    # Define the number of pages per book
    pages_per_book = 10

    # Calculate the total number of pages Janine read
    total_pages = (last_month_books + this_month_books) * pages_per_book

    # Display the total number of pages Janine read
    result = total_pages
    return result

print(solution())