def solution():
    """Miss Grayson's class raised $50 for their field trip. Aside from that, each of her students contributed $5 each. There are 20 students in her class, and the cost of the trip is $7 for each student. After all the field trip costs were paid, how much is left in Miss Grayson's class fund?"""
    field_trip_fund = 50
    student_contribution = 5
    num_students = 20
    cost_per_student = 7
    total_cost = num_students * cost_per_student
    remaining_fund = field_trip_fund + (num_students * student_contribution) - total_cost
    result = remaining_fund
    return result

print(solution())