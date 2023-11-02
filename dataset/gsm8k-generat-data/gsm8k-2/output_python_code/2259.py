def solution():
    """A special school has a deaf-student population 3 times its blind-student population. If there are 180 students in total, how many blind students are there?"""
    total_students = 180
    deaf_students = 3 * blind_students
    total_populations = 4
    blind_students = total_students / total_populations
    result = blind_students
    return result

print(solution())