def solution():
    """The total number of books on four shelves, with 400 books each, is the same as the distance in miles that Karen bikes back to her home from the library. Calculate the total distance that Karen covers if she bikes from her home to the library and back."""
    books_per_shelf = 400
    total_books = books_per_shelf * 4
    distance_per_book = 0.1  # Assumed distance covered per book
    total_distance = total_books * distance_per_book * 2  # Distance covered in round trip
    result = total_distance
    return result

print(solution())