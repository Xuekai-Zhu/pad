def solution():
    
    total_students = 3000
    over_16_students = total_students / 2
    over_16_male_students = over_16_students / 4
    under_16_students = total_students / 2 - over_16_male_students
    under_16_male_students = under_16_students / 2
    total_female_students = over_16_male_students + under_16_male_students
    result = total_female_students
    return result

print(solution())