def solution():
    """Evan owns 40 fewer books than the number he had 2 years ago. Evan will have 60 more than five times as many books as he owns now in five years. If Evan had 200 books two years ago, calculate the total number of books he will have in five years."""
    # Define the number of books Evan had 2 years ago
    books_two_years_ago = 200

    # Calculate the number of books Evan owns now
    current_books = books_two_years_ago - 40

    # Calculate the number of books Evan will have in 5 years
    future_books = 5 * (current_books * 5 + 60)

    # Calculate the total number of books Evan will have in 5 years
    total_books = current_books + future_books

    # Display the total number of books
    result = total_books
    return result

print(solution())