def solution():
     books_read_last_month = 5
     books_read_this_month = books_read_last_month * 2
     pages_per_book = 10
     total_pages_read = (books_read_last_month + books_read_this_month) * pages_per_book
     result = total_pages_read
     return result

print(solution())