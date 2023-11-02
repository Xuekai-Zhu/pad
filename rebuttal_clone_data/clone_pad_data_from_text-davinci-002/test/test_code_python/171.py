def solution():
    workers = 6
    warehouse_workers = 4
    manager_workers = 2
    wage_warehouse = 15
    wage_manager = 20
    hours_worked = 8
    days_worked = 25
    fica_tax = 0.1
    warehouse_wages = (wage_warehouse * hours_worked * days_worked) * warehouse_workers
    manager_wages = (wage_manager * hours_worked * days_worked) * manager_workers
    total_wages = warehouse_wages + manager_wages
    total_taxes = total_wages * fica_tax
    total_cost = total_wages + total_taxes
    result = total_cost
    
    return result

print(solution())