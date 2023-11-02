def solution():
    
    total_cost = 100
    boss_contribution = 15
    todd_contribution = 2 * boss_contribution
    remaining_cost = total_cost - boss_contribution - todd_contribution
    num_employees = 5
    employee_contribution = remaining_cost / num_employees
    result = employee_contribution
    return result

print(solution())