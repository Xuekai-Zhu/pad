def solution():
    initial_donation = 300
    new_donations = 10 * 5
    books_borrowed = 140

    # Calculate the total number of books in the store
    total_books = initial_donation + new_donations - books_borrowed
    result = total_books
    return result

print(solution())