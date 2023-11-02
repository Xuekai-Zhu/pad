def solution():
     fantasy_books = 4
     literature_books = fantasy_books / 2
     books_sold_fantasy = 5
     books_sold_literature = 8
     total_books_sold = books_sold_fantasy + books_sold_literature
     total_sales = (fantasy_books * books_sold_fantasy) + (literature_books * books_sold_literature)
     days = 5
     result = total_sales * days
     return result

print(solution())