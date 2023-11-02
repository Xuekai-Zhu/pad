def solution():
    """John is a hack author. He writes a book every 2 months. He has been writing for 20 years and has earned an average of $30,000 per book. How much money has he made writing?"""
    
    # 1 year = 12 months
    # 20 years = 240 months
    # 1 book every 2 months = 120 books
    
    books_written = 120
    earnings_per_book = 30000
    total_earnings = books_written * earnings_per_book
    
    result = total_earnings
    return result

print(solution())