def solution():
    # Calculate the number of adult books
    adult_books = 104

    # Calculate the percentage of books for children
    children_percentage = 35

    # Calculate the total number of books
    total_books = (adult_books / (100 - children_percentage)) * 100
    result = total_books
    return result

print(solution())