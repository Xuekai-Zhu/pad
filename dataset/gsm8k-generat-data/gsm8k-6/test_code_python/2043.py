def solution():
    # Calculate the number of books each person read last month
    william_books_last_month = 6
    brad_books_last_month = 3 * william_books_last_month

    # Calculate the number of books each person read this month
    brad_books_this_month = 8
    william_books_this_month = 2 * brad_books_this_month

    # Calculate the total number of books each person read across the two months
    total_books_william = william_books_last_month + william_books_this_month
    total_books_brad = brad_books_last_month + brad_books_this_month

    # Determine who read more books and by how much
    if total_books_william > total_books_brad:
        difference = total_books_william - total_books_brad
        result = "William read more by {} books".format(difference)
    else:
        difference = total_books_brad - total_books_william
        result = "Brad read more by {} books".format(difference)
    return result

print(solution())