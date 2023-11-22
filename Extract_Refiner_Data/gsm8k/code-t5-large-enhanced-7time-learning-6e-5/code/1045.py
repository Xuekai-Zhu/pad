def solution():
    
    # Define the total number of books
    total_books = 50

    # Calculate the number of books written in English
    english_books = total_books / 2

    # Calculate the number of books written in German
    german_books = total_books * 0.1

    # Calculate the number of books written in Spanish
    spanish_books = total_books - english_books - german_books

    # Display the number of books written in Spanish
    result = spanish_books
    return result

print(solution())