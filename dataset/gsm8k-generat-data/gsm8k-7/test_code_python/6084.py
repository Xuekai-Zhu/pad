def solution():
    num_girls = 15
    num_boys = 10
    total_students = num_girls + num_boys
    total_books = 375

    # Calculate the number of books each student gets
    num_books_per_student = total_books / total_students

    # Calculate the number of books the girls get
    num_books_girls = num_girls * num_books_per_student
    result = num_books_girls
    return result

print(solution())