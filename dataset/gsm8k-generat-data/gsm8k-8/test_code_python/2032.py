def solution():
    # Define the initial number of books
    initial_books = 250

    # Subtract the number of books taken out on Tuesday
    remaining_books = initial_books - 120

    # Add the number of books returned on Wednesday
    remaining_books += 35

    # Subtract the number of books taken out on Thursday
    remaining_books -= 15

    result = remaining_books
    return result

print(solution())