def solution():
    # Number of books William read last month
    william_books_last_month = 6

    # Number of books Brad read last month
    brad_books_last_month = 3 * william_books_last_month

    # Number of books William read this month
    william_books_this_month = 2 * 8  # William read twice as much as Brad, who read 8 books this month

    # Total number of books William has read over two months
    william_total_books = william_books_last_month + william_books_this_month

    # Total number of books Brad has read over two months
    brad_total_books = brad_books_last_month + 8

    if william_total_books > brad_total_books:
        result = "William has read more across the two months by " + str(william_total_books - brad_total_books) + " books."
    elif brad_total_books > william_total_books:
        result = "Brad has read more across the two months by " + str(brad_total_books - william_total_books) + " books."
    else:
        result = "They have read the same number of books across the two months."

    return result

print(solution())