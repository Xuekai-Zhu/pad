def solution():
    """Casey is trying to decide which employee she wants to hire. One employee works for $20 an hour. 
    The other employee works for $22 an hour, but Casey would also get a $6/hour subsidy from the government for hiring 
    a disabled worker. How much money per week would Casey save by hiring the cheaper employee, if they both work 40 hours per week?"""
    hourly_wage1 = 20
    hourly_wage2 = 22
    subsidy = 6
    hours_per_week = 40
    weekly_cost1 = hourly_wage1 * hours_per_week
    weekly_cost2 = (hourly_wage2 - subsidy) * hours_per_week
    savings = weekly_cost1 - weekly_cost2
    result = savings
    return result

print(solution())