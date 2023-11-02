def solution():
    """Mrs. Finley's class has 24 students, and Mr. Johnson's class has 10 more than half the number in Mrs. Finley's class. How many students are in Mr. Johnson's class?"""
    # Define the number of students in Mrs. Finley's class
    finley_students = 24

    # Calculate the number of students in Mr. Johnson's class
    johnson_students = int(0.5 * finley_students) + 10

    # Display the number of students in Mr. Johnson's class
    result = johnson_students
    return result

print(solution())