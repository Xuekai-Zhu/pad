def solution():
    """Hadley loves to do volunteer work at the local library. On a certain day, she neatly arranges 100 books on the shelf. By lunchtime, a certain number of books had been borrowed. She added 40 more books to the same shelf. By evening, 30 more books had been borrowed. If the shelf had 60 books remaining by the evening, how many books had been borrowed by lunchtime?"""
    # Define the initial number of books and the number borrowed by lunchtime
    initial_books = 100
    borrowed_lunchtime = None

    # Calculate the number of books remaining after the addition before evening
    books_after_addition = initial_books + 40

    # Calculate the number of books borrowed by evening
    borrowed_evening = books_after_addition - 60

    # Calculate the number of books borrowed by lunchtime
    borrowed_lunchtime = borrowed_evening - 30

    result = borrowed_lunchtime
    return result

print(solution())