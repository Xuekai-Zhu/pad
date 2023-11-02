def solution():
    """In a factory, there are 300 employees. 200 of them earn $12 per hour. Of the rest, 40 of them earn $14 per hour. All others earn $17 per hour. What is the cost to employ all these people for one 8-hour long shift?"""
    # Define the number of employees and their hourly wages
    num_employees = 300
    wage1 = 12
    wage2 = 14
    wage3 = 17

    # Calculate the cost of employing the employees for one hour
    cost1 = 200 * wage1
    cost2 = 40 * wage2
    cost3 = (num_employees - 240) * wage3
    total_cost_hour = cost1 + cost2 + cost3

    # Calculate the cost of employing the employees for one 8-hour long shift
    total_cost_shift = total_cost_hour * 8

    result = total_cost_shift
    return result

print(solution())