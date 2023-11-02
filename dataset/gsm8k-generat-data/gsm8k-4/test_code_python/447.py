def solution():
    """Megan has read 32 books this year. Kelcie has read 1/4 the amount of books that Megan has read.
    Greg has read 9 more than twice the number of books that Kelcie has read. How many books total have Megan, Kelcie, and Greg read?"""
    # Define the number of books Megan has read
    megan_books = 32

    # Calculate the number of books Kelcie has read
    kelcie_books = megan_books / 4

    # Calculate the number of books Greg has read
    greg_books = 9 + (2 * kelcie_books)

    # Calculate the total number of books read
    total_books = megan_books + kelcie_books + greg_books

    # Return the result
    result = total_books
    return result

print(solution())