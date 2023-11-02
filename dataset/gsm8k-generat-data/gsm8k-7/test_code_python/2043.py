def solution():
    # Calculate the total number of books William read last month
    william_books_last_month = 6

    # Calculate the total number of books Brad read last month
    brad_books_last_month = william_books_last_month * 3

    # Calculate the total number of books William read this month
    william_books_this_month = brad_books_last_month * 2

    # Calculate the total number of books Brad read this month
    brad_books_this_month = 8

    # Calculate the total number of books each person has read
    total_william_books = william_books_last_month + william_books_this_month
    total_brad_books = brad_books_last_month + brad_books_this_month

    # Determine who has read more
    if total_william_books > total_brad_books:
        difference = total_william_books - total_brad_books
        result = "William has read more by {} books".format(difference)
    elif total_brad_books > total_william_books:
        difference = total_brad_books - total_william_books
        result = "Brad has read more by {} books".format(difference)
    else:
        result = "Both William and Brad have read the same number of books"

    return result

print(solution())