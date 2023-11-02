def solution():
    
    total_students = 24
    before_lunch = total_students / 3
    after_lunch = before_lunch + 10
    remaining_students = total_students - after_lunch
    result = remaining_students
    return result

print(solution())