def solution():
    """A special school has a deaf-student population 3 times its blind-student population. If there are 180 students in total, how many blind students are there?"""
    # Define the ratio of deaf students to blind students
    deaf_blind_ratio = 3

    # Calculate the total number of students
    total_students = 180

    # Calculate the sum of the parts of the ratio
    ratio_sum = 1 + deaf_blind_ratio

    # Calculate the number of blind students
    blind_students = (1 / ratio_sum) * total_students

    # Display the number of blind students
    result = blind_students
    return result

print(solution())