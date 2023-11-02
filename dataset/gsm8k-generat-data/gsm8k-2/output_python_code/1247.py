def solution():
    """Mrs. Finley's class has 24 students, and Mr. Johnson's class has 10 more than half the number in Mrs. Finley's class. How many students are in Mr. Johnson's class?"""
    finley_students = 24
    johnson_students = (finley_students / 2) + 10
    result = johnson_students
    return result

print(solution())