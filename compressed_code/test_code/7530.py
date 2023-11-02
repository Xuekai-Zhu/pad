def solution():
    
    total_students = 1800
    percentage_foreign = 30
    foreign_students = total_students * (percentage_foreign / 100)
    new_foreign_students = 200
    total_foreign_students = foreign_students + new_foreign_students
    result = total_foreign_students
    return result

print(solution())