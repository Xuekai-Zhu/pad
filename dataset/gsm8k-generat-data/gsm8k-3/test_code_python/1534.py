def solution():
    """A library has a number of books. 35% of them are intended for children and 104 of them are for adults. How many books are in the library?"""
    # Define the percentage of books intended for children and the number of books for adults
    CHILD_BOOK_PERCENTAGE = 0.35
    ADULT_BOOK_COUNT = 104

    # Calculate the total number of books in the library
    total_books = ADULT_BOOK_COUNT / (1 - CHILD_BOOK_PERCENTAGE)

    # Display the total number of books
    result = total_books
    return result

print(solution())