def solution():
    num_students = 24
    num_before_lunch = num_students / 3
    num_after_lunch = num_before_lunch + 10
    num_taken = num_before_lunch + num_after_lunch
    num_not_taken = num_students - num_taken
    result = num_not_taken
    return result

print(solution())