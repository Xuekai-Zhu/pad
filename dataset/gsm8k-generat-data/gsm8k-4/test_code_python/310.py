def solution():
    """Janet hires six employees. Four of them are warehouse workers who make $15/hour, and the other two are managers who make $20/hour. Janet has to pay 10% of her workers' salaries in FICA taxes. If everyone works 25 days a month and 8 hours a day, how much does Janet owe total for their wages and taxes for one month?"""
    # Define the wages for warehouse workers and managers
    warehouse_worker_wage = 15
    manager_wage = 20

    # Define the number of warehouse workers and managers
    warehouse_workers = 4
    managers = 2

    # Calculate the total wages to be paid to all employees
    total_wages = (warehouse_worker_wage * 8 * 25 * warehouse_workers) + (manager_wage * 8 * 25 * managers)

    # Calculate the total taxes to be paid
    total_taxes = total_wages * 0.1

    # Calculate the total amount Janet owes for wages and taxes
    total_owed = total_wages + total_taxes

    # return the result
    result = total_owed
    return result

print(solution())