def solution():
    """John is a hack author. He writes a book every 2 months. He has been writing for 20 years and has earned an average of $30,000 per book. How much money has he made writing?"""
    books_per_year = 6
    years_writing = 20
    total_books = books_per_year * years_writing
    earnings_per_book = 30000
    total_earnings = total_books * earnings_per_book
    result = total_earnings
    return result

print(solution())