def solution():
    """Sabrina went to the library and found a historical series novel called The Rangers Apprentice. There are 14 books in the series, and each book has 200 pages. She read four books in a month and half the number of books remaining in the second month. What's the total number of pages Sabrina has to read to finish the whole series?"""
    # Define the number of books in the series and the number of pages per book
    NUM_BOOKS = 14
    PAGES_PER_BOOK = 200

    # Calculate the number of books Sabrina has left to read
    books_left = NUM_BOOKS - 4 - (NUM_BOOKS - 4) / 2

    # Calculate the total number of pages Sabrina has to read to finish the series
    total_pages = books_left * PAGES_PER_BOOK

    # Display the total number of pages
    result = total_pages
    return result

print(solution())