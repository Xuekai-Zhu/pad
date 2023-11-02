def solution():
    employee_1_wage = 20
    employee_2_wage = 22
    subsidy_amount = 6
    hours_worked = 40
    cost_1 = employee_1_wage * hours_worked
    cost_2 = (employee_2_wage * hours_worked) - (subsidy_amount * hours_worked)
    savings = cost_2 - cost_1
    result = savings
    return result

print(solution())