def solution():
    """Tracy has a charity book collection store from which she receives book donations from members of her town. Any person who wants to borrow a book is free to do so as long as they return the book after they've finished reading. She has already received 300 book donations. If ten people come and donate five books each in a week, and a total of 140 books are borrowed by other people to read, calculate the total number of books she has remaining in the store?"""
    # Define the initial number of books in the store
    initial_books = 300

    # Calculate the number of books donated by ten people who donated five books each
    donated_books = 10 * 5

    # Calculate the total number of books in the store
    total_books = initial_books + donated_books - 140

    # Return the result
    result = total_books
    return result

print(solution())