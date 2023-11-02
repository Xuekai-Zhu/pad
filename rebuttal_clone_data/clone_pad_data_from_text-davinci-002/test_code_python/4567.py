def solution():
    total_books = 743
    books_sold_store = 37
    books_sold_online = 128
    books_received = 160
    books_left = total_books - books_sold_store - books_sold_online + books_received
    result = books_left
    return result

print(solution())