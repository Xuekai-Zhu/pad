def solution():
    books_owned = 10
    books_lost = 2
    pages_per_book = 100
    pages_left = (books_owned - books_lost) * pages_per_book
    result = pages_left
    return result

print(solution())