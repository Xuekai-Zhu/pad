def solution():
    total_students = 50
    free_lunch_percent = 0.4  # 40% of the students
    paid_lunch_percent = 1 - free_lunch_percent  # 60% of the students
    total_cost = 210

    # Calculate the cost per paying student
    paid_student_cost = total_cost / (total_students * paid_lunch_percent)
    result = paid_student_cost
    return result

print(solution())