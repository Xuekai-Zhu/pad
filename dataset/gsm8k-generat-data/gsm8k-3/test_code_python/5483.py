def solution():
    """The total number of books on four shelves, with 400 books each, is the same as the distance in miles that Karen bikes back to her home from the library. Calculate the total distance that Karen covers if she bikes from her home to the library and back."""
    # Calculate the total number of books
    total_books = 4 * 400

    # Calculate the total distance Karen bikes
    distance = total_books / 5280 * 2

    # Display the total distance
    result = distance
    return result

print(solution())