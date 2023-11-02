def solution():
    
    starting_books = 72
    book_club_books = 12
    bookstore_books = 5
    yard_sale_books = 2
    daughter_books = 1
    mother_books = 4
    donated_books = 12
    sold_books = 3
    total_books = (starting_books + book_club_books + bookstore_books + yard_sale_books
                   + daughter_books + mother_books - donated_books - sold_books)
    result = total_books
    return result

print(solution())