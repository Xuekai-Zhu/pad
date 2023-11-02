def solution():
    """Casey is trying to decide which employee she wants to hire. One employee works for $20 an hour. The other employee works for $22 an hour, but Casey would also get a $6/hour subsidy from the government for hiring a disabled worker. How much money per week would Casey save by hiring the cheaper employee, if they both work 40 hours per week?"""
    # Define the hourly rates
    rate1 = 20
    rate2 = 22

    # Define the hours worked
    hours = 40

    # Calculate the weekly cost of each employee
    cost1 = rate1 * hours
    cost2 = (rate2 - 6) * hours

    # Calculate the amount saved per week by hiring the cheaper employee
    savings = cost1 - cost2

    # Display the amount saved per week
    result = savings
    return result

print(solution())