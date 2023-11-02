def solution():
    """A special school for deaf and blind students has a deaf student population three times the size of blind student population. If the number of deaf students is 180, how many students are there altogether?"""
    # Define the ratio of deaf students to blind students
    ratio_deaf_blind = 3

    # Calculate the number of blind students
    deaf_students = 180
    blind_students = deaf_students / ratio_deaf_blind

    # Calculate the total number of students
    total_students = deaf_students + blind_students

    # Return the result
    result = total_students
    return result

print(solution())