def solution():
    
    # Define the number of books each person has
    dolly_books = 2
    pandora_books = 1

    # Calculate the total number of books read by Dolly and Pandora
    total_books_read = (dolly_books + pandora_books) * 2

    # Calculate the total number of books left to read
    total_books_left = total_books_read - dolly_books - pandora_books

    # Display the total number of books left to read
    result = total_books_left
    return result

print(solution())