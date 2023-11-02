def solution():
    
    field_trip_fund = 50
    student_contribution = 5
    num_students = 20
    cost_per_student = 7
    total_cost = num_students * cost_per_student
    remaining_fund = field_trip_fund + (num_students * student_contribution) - total_cost
    result = remaining_fund
    return result

print(solution())