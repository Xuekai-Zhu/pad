def solution():
    total_cost = 100
    boss_contribution = 15
    todd_contribution = 2 * boss_contribution
    num_remaining_employees = 5
    remaining_cost = total_cost - boss_contribution - todd_contribution
    cost_each_employee = remaining_cost / num_remaining_employees
    result = cost_each_employee
    return result

print(solution())