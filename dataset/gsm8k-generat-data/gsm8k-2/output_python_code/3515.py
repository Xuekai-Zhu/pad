def solution():
    """In one of the teacher's meetings, it was agreed that each class will contribute $90 for a school activity. The class of Miss Evans has $14 class funds and they decided to use it to lessen the contribution of each student. If the remaining amount will be divided among 19 students, how much will each student contribute?"""
    total_contribution = 90
    class_funds = 14
    remaining_amount = total_contribution - class_funds
    num_students = 19
    per_student_contribution = remaining_amount / num_students
    result = per_student_contribution
    return result

print(solution())