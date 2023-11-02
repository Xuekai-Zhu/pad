def solution():
    """Elmo has 3 times as many books as his sister, Laura. Laura has twice as many books as her brother, Stu. If Elmo has 24 books, how many books does Stu have?"""
    # Define Elmo's number of books and the ratios of books between Elmo, Laura, and Stu
    elmo_books = 24
    elmo_laura_ratio = 3
    laura_stu_ratio = 2

    # Calculate Laura's number of books using Elmo-Laura ratio
    laura_books = elmo_books / elmo_laura_ratio

    # Calculate Stu's number of books using Laura-Stu ratio
    stu_books = laura_books / laura_stu_ratio

    # Display Stu's number of books
    result = stu_books
    return result

print(solution())