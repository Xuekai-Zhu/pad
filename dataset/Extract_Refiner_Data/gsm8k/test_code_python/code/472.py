def solution():
    
    total_spent = 300
    book_price = 15
    total_books = total_spent / book_price
    num_kids = 4
    books_per_child = total_books / num_kids
    result = books_per_child
    return result

print(solution())