def solution():
    num_students = 4
    total_time = num_students * 30  # average completion time of all four runners
    last_three_avg = 35  # average completion time of the last three students

    # Calculate the total completion time of the last three students
    last_three_total = last_three_avg * (num_students-1)  # (num_students-1) because we exclude the first student

    # Calculate the completion time of the first student
    first_student_time = total_time - last_three_total

    result = first_student_time
    return result

print(solution())