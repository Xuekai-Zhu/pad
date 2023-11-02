def solution():
    num_warehouse_workers = 4
    warehouse_worker_wage = 15

    num_managers = 2
    manager_wage = 20

    fica_tax_rate = 0.1  # 10% FICA tax rate

    num_working_days = 25
    num_working_hours_per_day = 8

    # Calculate the total wages for all workers
    total_wages = (num_warehouse_workers * warehouse_worker_wage * num_working_days * num_working_hours_per_day) + (
            num_managers * manager_wage * num_working_days * num_working_hours_per_day)

    # Calculate the total FICA taxes Janet owes
    total_fica_taxes = total_wages * fica_tax_rate

    # Calculate the total amount Janet owes for wages and taxes
    total_owed = total_wages + total_fica_taxes
    result = total_owed
    return result

print(solution())