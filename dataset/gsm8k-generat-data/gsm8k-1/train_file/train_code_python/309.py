def solution():
    """Janet hires six employees. Four of them are warehouse workers who make $15/hour, and the other two are managers who make $20/hour. Janet has to pay 10% of her workers' salaries in FICA taxes. If everyone works 25 days a month and 8 hours a day, how much does Janet owe total for their wages and taxes for one month?"""
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