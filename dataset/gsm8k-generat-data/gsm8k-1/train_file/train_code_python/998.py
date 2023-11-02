def solution():
    """Miss Grayson's class raised $50 for their field trip. Aside from that, each of her students contributed $5 each. There are 20 students in her class, and the cost of the trip is $7 for each student. After all the field trip costs were paid, how much is left in Miss Grayson's class fund?"""
    initial_fund = 50
    students = 20
    cost_per_student = 7
    student_contributions = students * 5
    total_cost = initial_fund + student_contributions + (students * cost_per_student)
    remaining_fund = initial_fund + student_contributions - total_cost
    result = remaining_fund
    return result

print(solution())