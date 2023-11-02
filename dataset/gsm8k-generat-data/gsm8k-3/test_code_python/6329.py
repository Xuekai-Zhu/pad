def solution():
    """The teachers divided the group of students into 3 groups of 8. But 2 students left early. How many remain?"""
    # Define the original number of students
    original_students = 3 * 8

    # Calculate the new number of students after 2 leave early
    remaining_students = original_students - 2

    # Display the remaining number of students
    result = remaining_students
    return result

print(solution())