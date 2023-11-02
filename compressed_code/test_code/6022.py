def solution():
    
    num_warehouse = 4
    num_managers = 2
    wage_warehouse = 15
    wage_manager = 20
    hours_worked = 8
    days_worked = 25
    total_hours = (num_warehouse*wage_warehouse + num_managers*wage_manager) * hours_worked * days_worked
    fica_tax = 0.10 * total_hours
    total_wages = total_hours + fica_tax
    result = total_wages
    return result

print(solution())