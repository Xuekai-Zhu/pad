def solution():
    """Tracy has a charity book collection store from which she receives book donations from members of her town. Any person who wants to borrow a book is free to do so as long as they return the book after they've finished reading. She has already received 300 book donations. If ten people come and donate five books each in a week, and a total of 140 books are borrowed by other people to read, calculate the total number of books she has remaining in the store?"""
    # Define the number of initial book donations
    initial_donations = 300

    # Define the number of books donated by 10 people
    books_donated = 5 * 10

    # Define the number of books borrowed
    books_borrowed = 140

    # Calculate the total number of books in the store
    total_books = initial_donations + books_donated - books_borrowed

    # Display the total number of books in the store
    result = total_books
    return result

print(solution())