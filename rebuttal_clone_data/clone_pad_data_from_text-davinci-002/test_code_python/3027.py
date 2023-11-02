def solution():
     starting_books = 72
     books_received = 12
     books_bought = 7
     books_given = 1
     books_sold = 3
     total_books = starting_books + books_received + books_bought - books_sold + books_given
     result = total_books
     return result

print(solution())