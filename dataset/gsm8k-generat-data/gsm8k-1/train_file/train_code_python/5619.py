def solution():
    """To make room for a new inventory of books, Gordon's local bookstore is offering 30% off any book that is over $22.00 and 20% off any book under $20.00. He buys several books with the following prices; $25.00, $18.00, $21.00, $35.00, $12.00 and $10.00. How much will he spend on books?"""
    books = [25.00, 18.00, 21.00, 35.00, 12.00, 10.00]
    discounted_books = []
    for book in books:
        if book > 22.00:
            discounted_books.append(book * 0.7)
        elif book < 20.00:
            discounted_books.append(book * 0.8)
        else:
            discounted_books.append(book)
    total_cost = sum(discounted_books)
    result = total_cost
    return result

print(solution())