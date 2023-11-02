def solution():
    
    warehouse_wage = 15
    manager_wage = 20
    num_warehouse = 4
    num_managers = 2
    total_employees = num_warehouse + num_managers
    hours_per_day = 8
    days_per_month = 25
    wage_before_tax = ((warehouse_wage * num_warehouse) + (manager_wage * num_managers)) * hours_per_day * days_per_month
    fica_tax = 0.1 * wage_before_tax
    total_wage = wage_before_tax + fica_tax
    result = total_wage
    return result

print(solution())