def solution():
    """William read 6 books last month and Brad read thrice as many books as William did. This month, in an effort to catch up, Williams read twice as much as Brad, who read 8 books. Who has read more across the two months, and by how much?"""
    # Define the number of books read by William and Brad in the first month
    w_books_month1 = 6
    b_books_month1 = w_books_month1 * 3

    # Define the number of books read by William and Brad in the second month
    b_books_month2 = 8
    w_books_month2 = b_books_month2 * 2

    # Calculate the total number of books read by each
    w_total_books = w_books_month1 + w_books_month2
    b_total_books = b_books_month1 + b_books_month2

    # Determine who has read more books and by how much
    if w_total_books > b_total_books:
        result = "William has read more books by {} book(s)".format(w_total_books - b_total_books)
    elif b_total_books > w_total_books:
        result = "Brad has read more books by {} book(s)".format(b_total_books - w_total_books)
    else:
        result = "William and Brad have read the same number of books"

    return result

print(solution())