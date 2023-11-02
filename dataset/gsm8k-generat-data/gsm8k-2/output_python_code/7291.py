def solution():
    """Marta was about to start the school year and needed to buy the necessary textbooks. She managed to buy five on sale, for $10 each. She had to order two textbooks online, which cost her a total of $40, and three she bought directly from the bookstore for a total of three times the cost of the online ordered books. How much in total did Martha spend on textbooks?"""
    on_sale_books = 5
    on_sale_price = 10
    online_books = 2
    online_price = 40
    bookstore_books = 3
    bookstore_price = online_price * 3
    total_price = (on_sale_books * on_sale_price) + online_price + (bookstore_books * bookstore_price)
    result = total_price
    return result

print(solution())