def solution():
    employees = 300
    employees_earning_12 = 200
    employees_earning_14 = 40
    employees_earning_17 = employees - employees_earning_12 - employees_earning_14
    cost_per_hour_12 = 12
    cost_per_hour_14 = 14
    cost_per_hour_17 = 17
    cost_for_12_employees = employees_earning_12 * cost_per_hour_12
    cost_for_14_employees = employees_earning_14 * cost_per_hour_14
    cost_for_17_employees = employees_earning_17 * cost_per_hour_17
    total_cost = cost_for_12_employees + cost_for_14_employees + cost_for_17_employees
    result = total_cost
    return result

print(solution())