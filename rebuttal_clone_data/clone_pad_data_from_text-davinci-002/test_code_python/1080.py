def solution():
    total_students = 180
    male_percentage = 70
    female_percentage = 100 - male_percentage
    female_students = total_students * (female_percentage / 100)
    male_students = total_students - female_students
    result = male_students
    return result

print(solution())