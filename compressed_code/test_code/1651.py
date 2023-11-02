def solution():
    
    students_per_year = 50
    first_year_students = 40
    total_years = 10
    total_students = first_year_students + (students_per_year * (total_years - 1))
    result = total_students
    return result

print(solution())