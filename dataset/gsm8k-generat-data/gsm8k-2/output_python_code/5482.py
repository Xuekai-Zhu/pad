def solution():
    """The total number of books on four shelves, with 400 books each, is the same as the distance in miles that Karen bikes back to her home from the library. Calculate the total distance that Karen covers if she bikes from her home to the library and back."""
    books_per_shelf = 400
    total_books = 4 * books_per_shelf
    distance_per_book = 0.1 # assuming each book adds 0.1 miles to the distance
    total_distance = total_books * distance_per_book * 2 # round trip distance
    result = total_distance
    return result

print(solution())