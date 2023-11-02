def solution():
    # Calculate the total number of books Brianna has for the year
    total_books = 2*12 + 6 + 8 + (8-2)  # Brianna reads 2 books a month, got 6 new books as a gift, bought 8 new books, plans to borrow 2 fewer than she bought
    books_to_reread = total_books - 24  # Brianna wants to have 24 books to read for the year (2 books a month), so she needs to reread this many
    result = books_to_reread
    return result

print(solution())