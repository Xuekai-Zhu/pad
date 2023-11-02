def solution():
    # Define the initial number of mystery books and the number of months in the year
    initial_books = 72
    months = 12

    # Calculate the number of books received from the book club
    book_club_books = months

    # Calculate the total number of books after the book club books are added
    total_books = initial_books + book_club_books

    # Add the books purchased at the bookstore and yard sales
    total_books += 5 + 2

    # Add the books received as gifts
    total_books += 1 + 4

    # Subtract the books donated and sold
    total_books -= 12 + 3

    result = total_books
    return result

print(solution())