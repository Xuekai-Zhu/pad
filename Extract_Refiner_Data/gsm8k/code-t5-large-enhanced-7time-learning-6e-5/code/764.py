def solution():
    
    # Define the number of books read by Ezra and Ahmed in one hour
    EZRA_books = 300
    AHMED_books = EZRA_books / 2

    # Calculate the total number of books read
    total_books = EZRA_books + AHMED_books + 150

    # Display the total number of books read
    result = total_books
    return result

print(solution())