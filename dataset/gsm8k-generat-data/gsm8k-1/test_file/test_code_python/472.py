def solution():
    """Sarah went to buy books from the store and spent $300 on the books. If each book was $15 and she gave an equal number of books to her 4 kids, how many books did each child get?"""
    total_spent = 300
    price_per_book = 15
    total_books = total_spent / price_per_book
    books_per_child = total_books / 4
    result = books_per_child
    return result

print(solution())