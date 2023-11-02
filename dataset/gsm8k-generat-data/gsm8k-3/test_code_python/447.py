def solution():
    """Megan has read 32 books this year. Kelcie has read 1/4 the amount of books that Megan has read. Greg has read 9 more than twice the number of books that Kelcie has read. How many books total have Megan, Kelcie, and Greg read?"""
    # Megan's number of books read
    megan_books = 32

    # Kelcie's number of books read
    kelcie_books = megan_books / 4

    # Greg's number of books read
    greg_books = 9 + 2 * kelcie_books

    # Total number of books read
    total_books = megan_books + kelcie_books + greg_books

    # Display the total number of books read
    result = total_books
    return result

print(solution())