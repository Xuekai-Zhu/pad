def solution():
    
    total_students = 3000
    over_16_students = total_students / 2
    male_over_16_students = over_16_students / 4
    male_under_16_students = total_students / 2
    male_under_16_students = under_16_students / 2
    total_female_students = total_students - (over_16_students + male_over_16_students + male_under_16_students)
    result = total_female_students
    return result

print(solution())