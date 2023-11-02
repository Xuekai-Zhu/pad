def solution():
    students = 25
    full_pay_students = students - 4  # 4 students paid half, so we subtract them from the total number of students.
    total_amount = (full_pay_students * 50) + (4 * 25)  # each full-paying student pays $50, each half-paying student pays $25.
    result = total_amount
    return result

print(solution())