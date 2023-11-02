def solution():
    total_students = 1800
    percent_foreigners = 30
    foreign_students = total_students * (percent_foreigners / 100)
    new_foreign_students = 200
    total_foreign_students = foreign_students + new_foreign_students
    result = total_foreign_students
    return result

print(solution())