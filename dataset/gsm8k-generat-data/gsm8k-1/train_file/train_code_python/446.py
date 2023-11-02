def solution():
    """Megan has read 32 books this year. Kelcie has read 1/4 the amount of books that Megan has read. Greg has read 9 more than twice the number of books that Kelcie has read. How many books total have Megan, Kelcie, and Greg read?"""
    megan_books = 32
    kelcie_books = megan_books / 4
    greg_books = 9 + 2 * kelcie_books
    total_books = megan_books + kelcie_books + greg_books
    result = total_books
    return result

print(solution())