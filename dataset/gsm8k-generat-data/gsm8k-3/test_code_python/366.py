def solution():
    """If Stu has 9 books and Albert has 4 times as many books as Stu, how many books do Stu and Albert have in total?"""
    # Define the number of books Stu has and the multiplier for Albert
    stu_books = 9
    albert_multiplier = 4

    # Calculate the number of books Albert has
    albert_books = stu_books * albert_multiplier

    # Calculate the total number of books
    total_books = stu_books + albert_books

    # Display the total number of books
    result = total_books
    return result

print(solution())