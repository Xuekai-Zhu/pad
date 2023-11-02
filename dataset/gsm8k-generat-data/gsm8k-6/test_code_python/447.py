def solution():
    # Calculate the number of books Kelcie has read
    kelcie_books = 1/4 * 32  # Kelcie has read 1/4 the amount of books that Megan has read

    # Calculate the number of books Greg has read
    greg_books = 9 + 2 * kelcie_books  # Greg has read 9 more than twice the number of books that Kelcie has read

    # Calculate the total number of books read by all three
    total_books = megan_books + kelcie_books + greg_books

    result = total_books
    return result

print(solution())