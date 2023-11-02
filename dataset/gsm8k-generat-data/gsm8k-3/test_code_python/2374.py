def solution():
    """In a factory, there are 300 employees. 200 of them earn $12 per hour. Of the rest, 40 of them earn $14 per hour. All others earn $17 per hour. What is the cost to employ all these people for one 8-hour long shift?"""
    # Define the number of employees and their hourly rates
    employees = 300
    rate1 = 12
    num1 = 200
    rate2 = 14
    num2 = 40
    rate3 = 17

    # Calculate the total cost to employ all the people for one 8-hour shift
    cost1 = rate1 * num1 * 8
    cost2 = rate2 * num2 * 8
    cost3 = (employees - num1 - num2) * rate3 * 8
    total_cost = cost1 + cost2 + cost3

    # Display the total cost
    result = total_cost
    return result

print(solution())