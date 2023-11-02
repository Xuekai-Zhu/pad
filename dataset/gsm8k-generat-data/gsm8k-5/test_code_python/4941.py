def solution():
    num_students_raising_20 = 10
    num_students_raising_30 = 20  # Total number of students minus the 10 raising $20 each
    total_raised_by_20 = num_students_raising_20 * 20
    total_raised_by_30 = num_students_raising_30 * 30
    total_raised = total_raised_by_20 + total_raised_by_30
    result = total_raised
    return result

print(solution())