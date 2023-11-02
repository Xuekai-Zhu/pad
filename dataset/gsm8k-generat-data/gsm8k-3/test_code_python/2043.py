def solution():
    """William read 6 books last month and Brad read thrice as many books as William did. This month, in an effort to catch up, Williams read twice as much as Brad, who read 8 books. Who has read more across the two months, and by how much?"""
    # Calculate the number of books read by William last month
    williams_books_last_month = 6

    # Calculate the number of books read by Brad last month
    brads_books_last_month = 3 * williams_books_last_month

    # Calculate the total number of books read by both of them last month
    total_books_last_month = williams_books_last_month + brads_books_last_month

    # Calculate the number of books read by Brad this month
    brads_books_this_month = 8

    # Calculate the number of books read by William this month
    williams_books_this_month = 2 * brads_books_this_month

    # Calculate the total number of books read by both of them this month
    total_books_this_month = williams_books_this_month + brads_books_this_month

    # Calculate the total number of books read by both of them across the two months
    total_books = total_books_last_month + total_books_this_month

    # Determine who read more across the two months and by how much
    if williams_books_last_month + williams_books_this_month > brads_books_last_month + brads_books_this_month:
        difference = williams_books_last_month + williams_books_this_month - (brads_books_last_month + brads_books_this_month)
        result = ("William read more books by", difference)
    elif williams_books_last_month + williams_books_this_month < brads_books_last_month + brads_books_this_month:
        difference = brads_books_last_month + brads_books_this_month - (williams_books_last_month + williams_books_this_month)
        result = ("Brad read more books by", difference)
    else:
        result = "They both read the same number of books"

    return result

print(solution())