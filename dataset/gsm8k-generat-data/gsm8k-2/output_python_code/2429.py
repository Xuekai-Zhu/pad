def solution():
    """Whitney bought 9 books about whales and 7 books about fish. She also bought 3 magazines. Each book cost $11 and each magazine cost $1. How much did Whitney spend in all?"""
    num_books = 16
    book_price = 11
    num_magazines = 3
    magazine_price = 1
    total_books_price = num_books * book_price
    total_magazines_price = num_magazines * magazine_price
    total_price = total_books_price + total_magazines_price
    result = total_price
    return result

print(solution())