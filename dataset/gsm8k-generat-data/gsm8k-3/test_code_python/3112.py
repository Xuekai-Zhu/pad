def solution():
    """There were students from three different schools taking part in a debate organized by the town's mayor on a stage. The first school had twice as many students as the second school, and the second school had 40 more students than the third school. If the third school had 200 students, and after the debate was over, every student shook the mayor's hand, calculate the total number of students who shook the mayor's hand on the stage."""
    # Define the number of students in the third school
    third_school = 200

    # Calculate the number of students in the second school
    second_school = third_school + 40

    # Calculate the number of students in the first school
    first_school = 2 * second_school

    # Calculate the total number of students on the stage
    total_students = first_school + second_school + third_school

    # Display the total number of students who shook the mayor's hand
    result = total_students
    return result

print(solution())