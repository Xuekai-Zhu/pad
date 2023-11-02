def solution():
    total_students = 24  # total number of students in the class
    before_lunch = total_students // 3  # number of students who had their portraits taken before lunch
    after_lunch = before_lunch + 10  # number of students who had their portraits taken after lunch
    remaining_students = total_students - after_lunch  # number of students who have not had their portraits taken yet
    result = remaining_students
    return result

print(solution())