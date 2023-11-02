def solution():
    """The total number of books on four shelves, with 400 books each, is the same as the distance in miles that Karen bikes back to her home from the library. Calculate the total distance that Karen covers if she bikes from her home to the library and back."""
    # Define the number of shelves and books per shelf
    shelves = 4
    books_per_shelf = 400

    # Calculate the total number of books
    total_books = shelves * books_per_shelf

    # Calculate the distance in miles per book
    distance_per_book = 1/total_books

    # Calculate the total distance Karen covers for the round trip
    total_distance = distance_per_book * total_books * 2

    # return the result
    result = total_distance
    return result

print(solution())