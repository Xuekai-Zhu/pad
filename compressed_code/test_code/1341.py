def solution():
    
    total_students = 300
    female_students = round(total_students * (2/3))
    male_students = total_students - female_students
    foreign_male_students = round(male_students / 10)
    non_foreign_male_students = male_students - foreign_male_students
    result = non_foreign_male_students
    return result

print(solution())