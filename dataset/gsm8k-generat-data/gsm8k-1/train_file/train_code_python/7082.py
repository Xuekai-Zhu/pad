def solution():
    """Lois has 40 books. She gives a fourth of her books to her nephew. From her remaining books, she donates a third of her books to the library.
    Then she purchases 3 new books from the book store. How many books does Lois have now?"""
    initial_books = 40
    nephew_share = initial_books // 4
    remaining_books = initial_books - nephew_share
    donated_books = remaining_books // 3
    new_books = 3
    final_books = remaining_books - donated_books + new_books
    result = final_books
    return result

print(solution())