def solution():
    """There are 250 books inside a library. On Tuesday, 120 books are taken out to be read by children. On Wednesday, 35 books are returned. On Thursday, another 15 books are withdrawn from the library. How many books are now in the library?"""
    # Define the initial number of books
    initial_books = 250

    # Calculate the number of books taken out on Tuesday and withdrawn on Thursday
    tues_thurs = 120 + 15

    # Calculate the number of books returned on Wednesday
    wed = 35

    # Calculate the final number of books in the library
    final_books = initial_books - tues_thurs + wed

    # return the result
    result = final_books
    return result

print(solution())