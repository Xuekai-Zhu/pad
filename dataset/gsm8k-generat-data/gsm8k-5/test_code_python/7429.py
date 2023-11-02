def solution():
    total_students = 28  # There are 28 students in the class
    absent_students = (2/7) * total_students  # Two-sevenths of the students were absent
    present_students = total_students - absent_students  # The number of present students is the difference between total and absent students
    result = present_students
    return result

print(solution())