def solution():
    books_bought = 6 + 4
    sarahs_books = 6
    paperback_books = sarahs_books / 3
    hardback_books = sarahs_books * 2
    brothers_books = paperback_books + hardback_books
    total_books = sarahs_books + brothers_books
    
    return total_books

print(solution())