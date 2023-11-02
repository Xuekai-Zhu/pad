def solution():
    books_per_month = 2  # Brianna reads 2 books a month
    total_new_books = 6 + 8 + (8 - 2)  # Brianna received 6 new books, bought 8, and borrowed 2 fewer than she bought
    total_books_needed = 12 - total_new_books  # Brianna wants to read 2 books a month for 12 months
    old_books_to_reread = total_books_needed * 2  # Brianna needs to reread 2 books per month, so multiply by total_books_needed

    result = old_books_to_reread
    return result

print(solution())