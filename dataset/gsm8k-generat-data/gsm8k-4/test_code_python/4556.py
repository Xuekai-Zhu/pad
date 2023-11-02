def solution():
    """The school is having a book-a-thon. The winning class gets a pizza party. The fifth grade has 20 students and one week to read as much as possible. The 6th grade already finished and read a total of 299 hours. How many hours does each student in 5th grade need to average per day to beat them by 1?"""
    # Define the number of students in the 5th grade
    fifth_grade_students = 20

    # Define the number of days in the book-a-thon
    bookathon_days = 7

    # Define the total number of hours the 6th grade read
    sixth_grade_hours = 299

    # Calculate the total number of hours the 5th grade needs to read to beat the 6th grade by 1 hour
    fifth_grade_hours = sixth_grade_hours + 1

    # Calculate the total number of hours the 5th grade needs to read per student
    per_student_hours = fifth_grade_hours / fifth_grade_students

    # Calculate the number of hours per day each student in the 5th grade needs to read to beat the 6th grade by 1 hour
    hours_per_day = per_student_hours / bookathon_days

    # Return the result
    result = round(hours_per_day, 2)
    return result

print(solution())