def solution():
    """In Mr. Bolton's class of 25 students, 2/5 of the students like maths, 1/3 of the remaining students like science, and the rest of the students like history. Calculate the combined total number of students who like history and those who like maths."""
    # Define the total number of students
    total_students = 25

    # Calculate the number of students who like maths
    maths_students = total_students * 2/5

    # Calculate the number of remaining students
    remaining_students = total_students - maths_students

    # Calculate the number of students who like science
    science_students = remaining_students * 1/3

    # Calculate the number of students who like history
    history_students = total_students - maths_students - science_students

    # Calculate the combined total number of students who like history and maths
    combined_total = maths_students + history_students

    # return the result
    result = combined_total
    return result

print(solution())