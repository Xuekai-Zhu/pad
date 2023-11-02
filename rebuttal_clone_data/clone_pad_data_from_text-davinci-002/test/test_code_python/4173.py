def solution():
    boris_books = 24
    cameron_books = 30
    boris_donation = boris_books // 4
    cameron_donation = cameron_books // 3
    boris_books_remaining = boris_books - boris_donation
    cameron_books_remaining = cameron_books - cameron_donation
    total_books = boris_books_remaining + cameron_books_remaining
    result = total_books
    return result

print(solution())