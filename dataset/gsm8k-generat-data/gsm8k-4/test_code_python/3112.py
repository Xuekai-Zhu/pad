def solution():
    """There were students from three different schools taking part in a debate organized by the town's mayor on a stage. The first school had twice as many students as the second school, and the second school had 40 more students than the third school. If the third school had 200 students, and after the debate was over, every student shook the mayor's hand, calculate the total number of students who shook the mayor's hand on the stage."""
    # Define the number of students in the third school
    third_school_students = 200

    # Calculate the number of students in the second school
    second_school_students = third_school_students + 40

    # Calculate the number of students in the first school
    first_school_students = second_school_students * 2

    # Calculate the total number of students on stage
    total_students = first_school_students + second_school_students + third_school_students

    # Every student shakes the mayor's hand, so the total number of students who shook the mayor's hand is the same as the total number of students
    result = total_students
    return result

print(solution())