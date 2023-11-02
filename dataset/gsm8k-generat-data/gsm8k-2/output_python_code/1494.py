def solution():
    """In a bookstore, a book costs $5. When Sheryll bought 10 books, she was given a discount of $0.5 each. How much did Sheryll pay in all?"""
    book_price = 5
    discount = 0.5
    discounted_price = book_price - discount
    total_books = 10
    total_price = (book_price * (total_books - (total_books // 2))) + (discounted_price * (total_books // 2))
    result = total_price
    return result

print(solution())