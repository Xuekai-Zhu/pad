def solution():
    """In Mr. Bolton's class of 25 students, 2/5 of the students like maths, 1/3 of the remaining students like science, and the rest of the students like history. Calculate the combined total number of students who like history and those who like maths."""
    # Define the total number of students in the class
    total_students = 25

    # Calculate the number of students who like maths
    math_students = int(2/5 * total_students)

    # Calculate the number of remaining students who don't like maths
    remaining_students = total_students - math_students

    # Calculate the number of students who like science from the remaining students
    science_students = int(1/3 * remaining_students)

    # Calculate the number of students who like history from the remaining students
    history_students = remaining_students - science_students

    # Calculate the combined total number of students who like history and maths
    total = math_students + history_students

    # Display the combined total number of students who like history and maths
    result = total
    return result

print(solution())