def solution():
     tuition_cost = 22000
     parents_contribution = tuition_cost/2
     scholarship = 3000
     student_loan = 2*scholarship
     total_contribution = parents_contribution + scholarship + student_loan
     semester_hours = 200
     hourly_wage = total_contribution/semester_hours
     result = hourly_wage
     
     return result

print(solution())