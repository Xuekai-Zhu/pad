def solution():
     initial_books = 300
     books_donated = 10 * 5
     books_borrowed = 140
     total_books = initial_books + books_donated - books_borrowed
     result = total_books
     return result

print(solution())