def solution():
     total_books = 56
     books_bought = total_books + 2
     shelves = 4
     books_per_shelf = 20
     total_books = shelves * books_per_shelf
     result = books_bought - total_books
     return result

print(solution())