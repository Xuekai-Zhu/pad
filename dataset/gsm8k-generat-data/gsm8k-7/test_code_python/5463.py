def solution():
    num_students = 30
    num_students_with_12_cans = num_students / 2
    num_students_with_4_cans = num_students - num_students_with_12_cans - 2  # subtract the 2 students who didn't collect any

    total_cans_collected = num_students_with_12_cans * 12 + num_students_with_4_cans * 4
    result = total_cans_collected
    return result

print(solution())