def solution():
    """In Mr. Bolton's class of 25 students, 2/5 of the students like maths, 1/3 of the remaining students like science, and the rest of the students like history. Calculate the combined total number of students who like history and those who like maths."""
    total_students = 25
    math_students = (2/5) * total_students
    remaining_students = total_students - math_students
    science_students = (1/3) * remaining_students
    history_students = remaining_students - science_students
    total_liking_maths_and_history = math_students + history_students

    return total_liking_maths_and_history

print(solution())