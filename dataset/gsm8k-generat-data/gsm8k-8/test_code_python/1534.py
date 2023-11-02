def solution():
    # Define the percentage of books intended for adults
    adult_percentage = 100 - 35

    # Calculate the total number of books for adults and children
    adult_books = 104
    total_books = adult_books * 100 / adult_percentage

    # Calculate the total number of books in the library
    result = total_books
    return result

print(solution())