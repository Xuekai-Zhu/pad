def solution():
    """Lois has 40 books. She gives a fourth of her books to her nephew. From her remaining books, she donates a third of her books to the library. Then she purchases 3 new books from the book store. How many books does Lois have now?"""
    initial_books = 40
    nephew_books = initial_books // 4
    remaining_books = initial_books - nephew_books
    donated_books = remaining_books // 3
    books_after_donation = remaining_books - donated_books
    books_after_purchase = books_after_donation + 3
    result = books_after_purchase
    return result

print(solution())