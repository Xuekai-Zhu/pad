def solution():
    """Adam teaches 50 students a year. How many students will Adam teach in 10 years if in the first year he only teaches 40 students?"""
    students_per_year = 50
    starting_students = 40
    total_years = 10
    total_students = (students_per_year * total_years) + starting_students
    result = total_students
    return result

print(solution())