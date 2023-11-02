def solution():
    # Calculate the number of books Tara needs to sell to save up $90
    target = 90
    saved = 10
    books_needed = (target - saved) / 5

    # Calculate the number of books Tara needs to sell after losing her savings
    books_remaining = (target / 2 - saved) / 5

    # Calculate the total number of books Tara needs to sell
    total_books = books_needed + books_remaining
    result = total_books
    return result

print(solution())