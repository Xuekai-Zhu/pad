def solution():
    """A special school has a deaf-student population 3 times its blind-student population. 
    If there are 180 students in total, how many blind students are there?"""
    total_students = 180
    deaf_population = 3
    blind_population = 1
    total_population = deaf_population + blind_population
    blind_students = (blind_population / total_population) * total_students
    result = blind_students
    return result

print(solution())