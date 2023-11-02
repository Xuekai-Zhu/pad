def solution():
     """Sabrina went to the library and found a historical series novel called The Rangers Apprentice. There are 14 books in the series, and each book has 200 pages. She read four books in a month and half the number of books remaining in the second month. What's the total number of pages Sabrina has to read to finish the whole series?"""
     total_books = 14
     pages_per_book = 200
     books_read_month_one = 4
     books_read_month_two = (total_books - books_read_month_one) / 2
     total_books_read = books_read_month_one + books_read_month_two
     total_pages_read = total_books_read * pages_per_book
     result = total_pages_read
     return result

print(solution())