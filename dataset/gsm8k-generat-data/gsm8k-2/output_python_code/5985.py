def solution():
    """Nancy wants to figure out if she can afford to apply to the University of Michigan. The tuition costs $22,000 per semester. Her parents can pay half the cost, and each semester Nancy can get a scholarship for $3,000 and a student loan for twice her scholarship amount. If Nancy can work a total of 200 hours during the semester, how many dollars does she have to make per hour to pay the rest of the tuition?"""
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