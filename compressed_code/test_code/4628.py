def solution():
    
    tuition = 22000
    parents_contribution = tuition / 2
    scholarship = 3000
    loan = 2 * scholarship
    total_student_contribution = tuition - parents_contribution - scholarship - loan
    hours_worked = 200
    hourly_wage = total_student_contribution / hours_worked
    result = hourly_wage
    return result

print(solution())