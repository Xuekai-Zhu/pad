def solution():
    """Evan owns 40 fewer books than the number he had 2 years ago. Evan will have 60 more than five times as many books as he owns now in five years. If Evan had 200 books two years ago, calculate the total number of books he will have in five years."""
    evan_books_2_years_ago = 200
    evan_books_now = evan_books_2_years_ago - 40
    evan_books_in_5_years = 5 * evan_books_now + 60
    total_books_in_5_years = evan_books_2_years_ago + evan_books_in_5_years
    result = total_books_in_5_years
    return result

print(solution())