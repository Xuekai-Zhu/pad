def solution():
    """For this month, Lily wants to finish reading twice as many books as she finished last month. If she finished reading 4 books last month, what will be the total number of books that she will finish for two months?"""
    # Define the number of books Lily finished last month
    books_last_month = 4

    # Calculate the number of books Lily wants to finish this month
    books_this_month = books_last_month * 2

    # Calculate the total number of books Lily will finish for two months
    total_books = books_last_month + books_this_month

    # Display the total number of books
    result = total_books
    return result

print(solution())