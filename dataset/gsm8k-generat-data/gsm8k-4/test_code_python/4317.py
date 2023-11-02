def solution():
    """For this month, Lily wants to finish reading twice as many books as she finished last month. If she finished reading 4 books last month, what will be the total number of books that she will finish for two months?"""
    # Define the number of books read last month
    last_month_books = 4

    # Calculate the number of books to be read this month
    this_month_books = 2 * last_month_books

    # Calculate the total number of books read in two months
    total_books = last_month_books + this_month_books

    # return the result
    result = total_books
    return result

print(solution())