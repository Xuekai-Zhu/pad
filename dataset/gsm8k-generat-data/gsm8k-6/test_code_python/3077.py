def solution():
    # Calculate the total number of books received after the ten people donated
    total_books_received = 300 + (10 * 5)  

    # Calculate the total number of books returned to the store
    total_books_returned = 140  

    # Calculate the remaining number of books in the store
    remaining_books = total_books_received - total_books_returned  
    result = remaining_books
    return result

print(solution())