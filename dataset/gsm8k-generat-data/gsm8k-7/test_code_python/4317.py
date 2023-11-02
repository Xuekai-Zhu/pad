def solution():
    books_last_month = 4
    target_ratio = 2  # Lily wants to double her books from last month
    total_months = 2  # Lily wants to finish books for two months
    total_books = (books_last_month * target_ratio) + books_last_month
    # Calculate the total number of books Lily wants to read for two months
    # (double the books from last month + last month's books)
    result = total_books
    return result

print(solution())