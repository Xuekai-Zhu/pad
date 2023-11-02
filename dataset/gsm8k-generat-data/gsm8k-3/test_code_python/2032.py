def solution():
    """There are 250 books inside a library. On Tuesday, 120 books are taken out to be read by children. On Wednesday, 35 books are returned. On Thursday, another 15 books are withdrawn from the library. How many books are now in the library?"""
    # Define the initial number of books
    initial_books = 250

    # Subtract the number of books taken out on Tuesday
    books = initial_books - 120

    # Add the number of books returned on Wednesday
    books += 35

    # Subtract the number of books taken out on Thursday
    books -= 15

    # Display the current number of books in the library
    result = books
    return result

print(solution())