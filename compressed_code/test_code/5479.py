def solution():
    
    initial_books = 40
    nephew_books = initial_books // 4
    remaining_books = initial_books - nephew_books
    donated_books = remaining_books // 3
    books_after_donation = remaining_books - donated_books
    books_after_purchase = books_after_donation + 3
    result = books_after_purchase
    return result

print(solution())