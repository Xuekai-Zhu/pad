def solution():
    """Nancy is returning her overdue books to the library. She owes $0.50 cents each on 8 books, plus a flat $2.00 fee for having at least one book that's over a week overdue. How much does she have to pay total?"""
    book_fee = 0.5
    num_books = 8
    overdue_fee = 2.0
    total_fee = (book_fee * num_books) + overdue_fee
    result = total_fee
    return result

print(solution())