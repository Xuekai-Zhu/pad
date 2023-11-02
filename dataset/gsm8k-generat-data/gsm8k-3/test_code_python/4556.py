def solution():
    """The school is having a book-a-thon. The winning class gets a pizza party. The fifth grade has 20 students and one week to read as much as possible. The 6th grade already finished and read a total of 299 hours. How many hours does each student in 5th grade need to average per day to beat them by 1?"""
    # Define the number of students in 5th grade and the total hours read by 6th grade
    students_5 = 20
    hours_6 = 299

    # Calculate the total hours 5th grade needs to read to beat 6th grade by 1 hour
    hours_5 = hours_6 + 20 * 7 * 1

    # Calculate the average hours per day each student in 5th grade needs to read
    hours_per_student = hours_5 / (20 * 7)

    # Display the required number of hours per day
    result = hours_per_student
    return result

print(solution())