def solution():
    """When Billy was first hired, he was paid at a rate of $10 per hour. After 2 months, he was given a raise of $0.50 per hour. On his first anniversary at work, he was given a raise of $1.00 per hour. Sally just started working at a different business, and her starting salary is $0.50 more per hour than Billy's starting salary was. If both Billy and Sally work 20 hours, how much more money will Billy earn than Sally, in dollars?"""
    billy_starting_salary = 10.00
    billy_2_month_raise = 0.50
    billy_anniversary_raise = 1.00
    billy_hourly_salary = billy_starting_salary + billy_2_month_raise + billy_anniversary_raise
    sally_starting_salary = billy_starting_salary + 0.50
    hours_worked = 20
    billy_earnings = billy_hourly_salary * hours_worked
    sally_earnings = sally_starting_salary * hours_worked
    difference = billy_earnings - sally_earnings
    result = difference
    return result

print(solution())