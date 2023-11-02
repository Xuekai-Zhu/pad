def solution():
    """Janet hires six employees. Four of them are warehouse workers who make $15/hour, and the other two are managers who make $20/hour. Janet has to pay 10% of her workers' salaries in FICA taxes. If everyone works 25 days a month and 8 hours a day, how much does Janet owe total for their wages and taxes for one month?"""
    # Define the wages of each type of employee
    WAREHOUSE_WAGE = 15
    MANAGER_WAGE = 20

    # Calculate the total number of hours worked by each employee per month
    hours_per_employee = 25 * 8

    # Calculate the total wage cost for the warehouse workers
    warehouse_wages = 4 * WAREHOUSE_WAGE * hours_per_employee

    # Calculate the total wage cost for the managers
    manager_wages = 2 * MANAGER_WAGE * hours_per_employee

    # Calculate the total wage cost for all employees
    total_wages = warehouse_wages + manager_wages

    # Calculate the FICA tax
    fica_tax = total_wages * 0.1

    # Calculate the total cost
    total_cost = total_wages + fica_tax

    # Display the total cost
    result = total_cost
    return result

print(solution())