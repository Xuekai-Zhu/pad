def solution():
    """Marta was about to start the school year and needed to buy the necessary textbooks. She managed to buy five on sale, for $10 each. She had to order two textbooks online, which cost her a total of $40, and three she bought directly from the bookstore for a total of three times the cost of the online ordered books. How much in total did Martha spend on textbooks?"""
    sale_books = 5
    sale_book_price = 10
    online_books = 2
    online_book_price = 40 / online_books
    bookstore_books = 3
    bookstore_book_price = (online_book_price * 3)
    total_cost = (sale_books * sale_book_price) + (online_books * online_book_price) + (bookstore_books * bookstore_book_price)
    result = total_cost
    return result

print(solution())