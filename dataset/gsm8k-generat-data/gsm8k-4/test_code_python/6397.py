def solution():
    """Casey is trying to decide which employee she wants to hire. One employee works for $20 an hour. The other employee works for $22 an hour, but Casey would also get a $6/hour subsidy from the government for hiring a disabled worker. How much money per week would Casey save by hiring the cheaper employee, if they both work 40 hours per week?"""
    # Define the hourly wages for both employees
    wage1 = 20
    wage2 = 22

    # Calculate the weekly wages for both employees
    weekly_wage1 = wage1 * 40
    weekly_wage2 = (wage2 - 6) * 40  # Subtract government subsidy from hourly wage

    # Calculate the difference in weekly wages
    difference = weekly_wage2 - weekly_wage1

    # Return the result
    result = difference
    return result

print(solution())