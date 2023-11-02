def solution():
    """Phil has 10 books that are all 100 pages each. He moves to a new home and during the move, 2 books are lost. How many pages worth of books does Phil have left?"""
    # Define the number of books and pages per book
    NUM_BOOKS = 10
    PAGES_PER_BOOK = 100

    # Define the number of lost books
    LOST_BOOKS = 2

    # Calculate the total number of pages before losing the books
    total_pages_before = NUM_BOOKS * PAGES_PER_BOOK

    # Calculate the total number of pages after losing the books
    total_pages_after = (NUM_BOOKS - LOST_BOOKS) * PAGES_PER_BOOK

    # Calculate the number of pages lost
    pages_lost = total_pages_before - total_pages_after

    # Display the number of pages remaining
    result = total_pages_after
    return result

print(solution())