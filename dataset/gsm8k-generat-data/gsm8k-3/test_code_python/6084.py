def solution():
    """There are 15 girls and 10 boys in Ms. Smith's class. She divided 375 books equally among them. How many books did all the girls get combined?"""
    # Define the number of girls and boys
    num_girls = 15
    num_boys = 10

    # Calculate the total number of students
    total_students = num_girls + num_boys

    # Calculate the number of books each student received
    books_per_student = 375 / total_students

    # Calculate the number of books all the girls received
    girl_books = num_girls * books_per_student

    # Display the number of books all the girls received
    result = girl_books
    return result

print(solution())