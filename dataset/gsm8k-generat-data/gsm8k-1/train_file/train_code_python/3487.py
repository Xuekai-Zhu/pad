def solution():
    """Evan owns 40 fewer books than the number he had 2 years ago. Evan will have 60 more than five times as many books as he owns now in five years. If Evan had 200 books two years ago, calculate the total number of books he will have in five years."""
    books_2_years_ago = 200
    current_books = books_2_years_ago - 40
    future_books = (5 * current_books) + 60
    total_books = future_books
    return total_books

print(solution())