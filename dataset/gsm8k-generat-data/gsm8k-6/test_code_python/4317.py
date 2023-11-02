def solution():
    # Calculate the total number of books Lily will finish in two months
    num_books_this_month = 4 * 2  # Lily wants to finish twice as many books as last month
    total_num_books = 4 + num_books_this_month  # add the number of books from last month and this month
    result = total_num_books
    return result

print(solution())