def solution():
     books = 40
     books_given = books / 4
     books_left = books - books_given
     books_donated = books_left / 3
     books_purchased = 3
     books_total = books_left - books_donated + books_purchased
     result = books_total
     return result

print(solution())