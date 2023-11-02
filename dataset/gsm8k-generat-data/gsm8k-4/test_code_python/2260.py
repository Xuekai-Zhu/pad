def solution():
    """A special school has a deaf-student population 3 times its blind-student population. If there are 180 students in total, how many blind students are there?"""
    # Define the total number of students
    total_students = 180

    # Let x be the number of blind students, then the number of deaf students is 3x
    # The total number of students is the sum of blind and deaf students
    # Therefore, we have the equation: x + 3x = 180
    # Solving for x, we get: 4x = 180 --> x = 45

    # The number of blind students is x
    result = 45
    return result

print(solution())