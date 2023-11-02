def solution():
    """Elmo has 3 times as many books as his sister, Laura. Laura has twice as many books as her brother, Stu. If Elmo has 24 books, how many books does Stu have?"""
    # Calculate the number of books Laura has
    laura_books = 24 / 3

    # Calculate the number of books Stu has
    stu_books = laura_books / 2

    # Return the result
    result = stu_books
    return result

print(solution())