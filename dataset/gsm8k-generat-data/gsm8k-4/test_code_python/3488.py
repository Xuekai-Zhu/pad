def solution():
    """Evan owns 40 fewer books than the number he had 2 years ago. Evan will have 60 more than five times as many books as he owns now in five years.
    If Evan had 200 books two years ago, calculate the total number of books he will have in five years."""
    # Define the number of books Evan had 2 years ago
    books_2_years_ago = 200

    # Calculate the number of books Evan owns now
    books_now = books_2_years_ago - 2 - 40

    # Calculate the number of books Evan will have in five years
    books_5_years = 5 * books_now + 60

    # return the result
    result = books_5_years
    return result

print(solution())