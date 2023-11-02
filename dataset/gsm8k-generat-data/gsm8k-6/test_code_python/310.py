def solution():
    # Calculate the total base wage for the warehouse workers
    warehouse_wage = 4 * 15 * 25 * 8  # 4 workers, earning $15/hour, working 25 days a month, 8 hours a day

    # Calculate the total base wage for the managers
    manager_wage = 2 * 20 * 25 * 8  # 2 managers, earning $20/hour, working 25 days a month, 8 hours a day

    # Calculate the total wage before FICA taxes
    total_wage = warehouse_wage + manager_wage

    # Calculate the amount of FICA taxes Janet has to pay
    FICA_tax = total_wage * 0.10  # 10% of the total wage

    # Calculate the total amount Janet owes for wages and taxes
    total_amount = total_wage + FICA_tax
    result = total_amount
    return result

print(solution())