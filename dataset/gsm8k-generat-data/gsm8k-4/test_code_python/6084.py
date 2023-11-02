def solution():
    """There are 15 girls and 10 boys in Ms. Smith's class. She divided 375 books equally among them. How many books did all the girls get combined?"""
    # Define the numbers of girls and boys in the class
    num_girls = 15
    num_boys = 10

    # Define the total number of students
    total_students = num_girls + num_boys

    # Define the total number of books
    total_books = 375

    # Calculate the number of books each student receives
    books_per_student = total_books // total_students

    # Calculate the number of books all the girls get combined
    total_girls_books = books_per_student * num_girls

    # return the result
    result = total_girls_books
    return result

print(solution())