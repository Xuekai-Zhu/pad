def solution():
    num_books = 10
    pages_per_book = 100
    books_lost = 2

    # Calculate the total number of pages before books were lost
    total_pages_before_loss = num_books * pages_per_book

    # Calculate the new total number of books after the loss
    num_books_left = num_books - books_lost

    # Calculate the total number of pages left
    total_pages_left = num_books_left * pages_per_book
    result = total_pages_left
    return result

print(solution())