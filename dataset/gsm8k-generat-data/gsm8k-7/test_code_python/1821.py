def solution():
    num_students = 24
    before_lunch = num_students / 3
    after_lunch = before_lunch + 10
    remaining_students = num_students - after_lunch
    result = remaining_students
    return result

print(solution())