def solution():
    """Jane bought pens for her three students. Each student received 62 red pens and 43 black pens. They pooled their pens together and took them from the pool whenever they needed them. After the first month, they had taken a total of 37 pens from the pool. After the second month, they had taken another 41 pens from the pool. Then Jane decided to split the remaining pens equally among them. How many pens will each student get now?"""
    red_pens_per_student = 62
    black_pens_per_student = 43
    total_pens_per_student = red_pens_per_student + black_pens_per_student
    total_students = 3
    total_pens_given = total_pens_per_student * total_students
    pens_taken_first_month = 37
    pens_taken_second_month = 41
    remaining_pens = total_pens_given - pens_taken_first_month - pens_taken_second_month
    pens_per_student_now = remaining_pens / total_students
    result = pens_per_student_now
    return result

print(solution())