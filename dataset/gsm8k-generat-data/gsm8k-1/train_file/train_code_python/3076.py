def solution():
    """
    Tracy has a charity book collection store from which she receives book donations from members of her town. 
    Any person who wants to borrow a book is free to do so as long as they return the book after they've finished reading. 
    She has already received 300 book donations. If ten people come and donate five books each in a week, 
    and a total of 140 books are borrowed by other people to read, calculate the total number of books she has remaining in the store?
    """
    # Initial number of books
    initial_books = 300

    # Donated books
    donated_books = 10 * 5

    # Borrowed books returned
    returned_books = 140

    # Total remaining books
    total_books = initial_books + donated_books - returned_books

    result = total_books
    return result

print(solution())