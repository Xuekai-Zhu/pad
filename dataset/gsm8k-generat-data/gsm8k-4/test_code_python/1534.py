def solution():
    """A library has a number of books. 35% of them are intended for children and 104 of them are for adults. How many books are in the library?"""
    # Define the percentage of books intended for children and the number of books for adults
    children_percentage = 0.35
    adult_books = 104

    # Calculate the total number of books in the library
    total_books = adult_books / (1 - children_percentage)

    # Round the result to the nearest whole number
    result = round(total_books)
    return result

print(solution())