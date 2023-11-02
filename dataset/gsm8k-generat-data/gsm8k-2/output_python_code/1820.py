def solution():
    """There are 24 students in the class. One-third had their school portraits taken before lunch. After lunch, but before gym class, 10 additional students had their portraits taken. After gym class, how many students have not yet had their picture taken?"""
    class_size = 24
    before_lunch = class_size // 3
    after_lunch = before_lunch + 10
    remaining = class_size - after_lunch
    result = remaining
    return result

print(solution())