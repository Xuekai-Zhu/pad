def solution():
    """Casey is trying to decide which employee she wants to hire. One employee works for $20 an hour. The other employee works for $22 an hour, but Casey would also get a $6/hour subsidy from the government for hiring a disabled worker. How much money per week would Casey save by hiring the cheaper employee, if they both work 40 hours per week?"""
    hourly_wage_employee_1 = 20
    hourly_wage_employee_2 = 22
    hourly_subsidy_employee_2 = 6
    hours_per_week = 40
    weekly_wage_employee_1 = hourly_wage_employee_1 * hours_per_week
    weekly_wage_employee_2 = (hourly_wage_employee_2 - hourly_subsidy_employee_2) * hours_per_week
    weekly_savings = weekly_wage_employee_1 - weekly_wage_employee_2
    result = weekly_savings
    return result

print(solution())