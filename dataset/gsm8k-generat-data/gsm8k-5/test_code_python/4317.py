def solution():
    last_month_books = 4  # Lily finished reading 4 books last month
    this_month_books = 2 * last_month_books  # Lily wants to finish reading twice as many books as last month

    # Calculate the total number of books Lily will finish in two months
    total_books = last_month_books + this_month_books
    result = total_books
    return result

print(solution())