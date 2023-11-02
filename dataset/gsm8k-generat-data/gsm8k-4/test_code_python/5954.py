def solution():
    """Tina's classroom has the same amount of students as Maura's. Zack's classroom has half the amount of total students between Tina and Maura's classrooms.
    How many students are there in total between the 3 classrooms if when Zack was sick there were 22 students in his class?"""
    # Define the number of students in Zack's class
    zack_students = 22

    # Calculate the total number of students in Tina and Maura's classes
    total_tm_students = (zack_students / 0.5)

    # Calculate the total number of students in all three classes
    total_students = total_tm_students + zack_students

    # Return the result
    result = total_students
    return result

print(solution())