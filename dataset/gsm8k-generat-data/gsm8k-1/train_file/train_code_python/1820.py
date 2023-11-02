def solution():
    """There are 24 students in the class. One-third had their school portraits taken before lunch. After lunch, but before gym class, 10 additional students had their portraits taken. After gym class, how many students have not yet had their picture taken?"""
    total_students = 24
    before_lunch = total_students / 3
    after_lunch = before_lunch + 10
    remaining_students = total_students - after_lunch
    result = remaining_students
    return result

print(solution())