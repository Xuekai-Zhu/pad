def solution():
    """The teachers divided the group of students into 3 groups of 8. But 2 students left early. How many remain?"""
    # Define the initial number of students
    initial_students = 24

    # Define the number of students who left early
    early_leavers = 2

    # Calculate the number of students remaining
    remaining_students = initial_students - early_leavers

    # Return the result
    result = remaining_students
    return result

print(solution())