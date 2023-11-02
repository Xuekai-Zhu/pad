def solution():
    """Hadley loves to do volunteer work at the local library. On a certain day, she neatly arranges 100 books on the shelf. By lunchtime, a certain number of books had been borrowed. She added 40 more books to the same shelf. By evening, 30 more books had been borrowed. If the shelf had 60 books remaining by the evening, how many books had been borrowed by lunchtime?"""
    # Define the initial number of books on the shelf
    initial_books = 100

    # Define the number of books added after lunchtime
    added_books = 40

    # Define the number of books remaining in the evening
    remaining_books = 60

    # Calculate the number of books borrowed by lunchtime
    borrowed_books = initial_books - remaining_books - added_books

    # Display the number of books borrowed by lunchtime
    result = borrowed_books
    return result

print(solution())