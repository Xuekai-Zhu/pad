def solution():
    # Define the initial number of books and the number borrowed by lunchtime
    initial_books = 100
    lunch_borrowed = x

    # Update the number of books after lunchtime and the number borrowed by evening
    books_after_lunch = initial_books - lunch_borrowed + 40
    evening_borrowed = books_after_lunch - 60

    # Solve for the number borrowed by lunchtime
    lunch_borrowed = initial_books - books_after_lunch + evening_borrowed
    result = lunch_borrowed
    return result

print(solution())