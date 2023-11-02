def solution():
    # Define the number of books and pages per book
    num_books = 10
    pages_per_book = 100

    # Calculate the total number of pages before the move
    total_pages_before = num_books * pages_per_book

    # Calculate the number of pages lost
    pages_lost = 2 * pages_per_book

    # Calculate the total number of pages after the move
    total_pages_after = total_pages_before - pages_lost
    result = total_pages_after
    return result

print(solution())