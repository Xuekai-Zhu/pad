def solution():
    """Phil has 10 books that are all 100 pages each. He moves to a new home and during the move, 2 books are lost. How many pages worth of books does Phil have left?"""
    # Define the number of books and pages per book
    num_books = 10
    pages_per_book = 100

    # Calculate the total number of pages before losing books
    total_pages = num_books * pages_per_book

    # Calculate the number of pages lost
    lost_pages = 2 * pages_per_book

    # Calculate the total number of pages remaining
    pages_left = total_pages - lost_pages

    # Display the result
    result = pages_left
    return result

print(solution())