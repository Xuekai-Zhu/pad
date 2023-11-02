def solution():
    total_cost = 100
    boss_contribution = 15
    todd_contribution = 2 * 15
    other_employees = 5
    total_contributed = total_cost - boss_contribution - todd_contribution
    contribution_per_employee = total_contributed / other_employees
    result = contribution_per_employee
    
    return result

print(solution())