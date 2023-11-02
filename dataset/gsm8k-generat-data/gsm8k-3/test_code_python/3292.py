def solution():
    """A special school for deaf and blind students has a deaf student population three times the size of blind student population. If the number of deaf students is 180, how many students are there altogether?"""
    # Define the ratio of deaf students to blind students
    RATIO = 3

    # Calculate the number of blind students
    blind_students = 180 // RATIO

    # Calculate the total number of students
    total_students = 180 + blind_students

    # Display the total number of students
    result = total_students
    return result

print(solution())