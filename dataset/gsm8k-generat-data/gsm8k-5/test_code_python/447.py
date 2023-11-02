def solution():
    megan_books = 32  # Megan has read 32 books
    kelcie_books = megan_books / 4  # Kelcie has read 1/4 of the number of books that Megan has read
    greg_books = 9 + 2 * kelcie_books  # Greg has read 9 more than twice the number of books Kelcie has read

    # Calculate the total number of books read
    total_books = megan_books + kelcie_books + greg_books
    result = total_books
    return result

print(solution())