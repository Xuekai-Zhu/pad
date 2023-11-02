def solution():
    """There are 28 students in a classroom. Half of them have 5 notebooks each and the other half have 3 notebooks each. How many notebooks in total are in the classroom?"""
    # Define the number of students and the number of notebooks per student for each group
    NUM_STUDENTS = 28
    NOTEBOOKS_1 = 5
    NOTEBOOKS_2 = 3

    # Calculate the number of students in each group
    num_students_1 = NUM_STUDENTS // 2
    num_students_2 = NUM_STUDENTS - num_students_1

    # Calculate the total number of notebooks in each group
    total_notebooks_1 = num_students_1 * NOTEBOOKS_1
    total_notebooks_2 = num_students_2 * NOTEBOOKS_2

    # Calculate the total number of notebooks in the classroom
    total_notebooks = total_notebooks_1 + total_notebooks_2

    # Display the total number of notebooks
    result = total_notebooks
    return result

print(solution())