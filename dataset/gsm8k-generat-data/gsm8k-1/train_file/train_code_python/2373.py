def solution():
    """In a factory, there are 300 employees. 200 of them earn $12 per hour. Of the rest, 40 of them earn $14 per hour. All others earn $17 per hour. What is the cost to employ all these people for one 8-hour long shift?"""
    num_employees = 300
    wage_1 = 12
    num_wage_1 = 200
    wage_2 = 14
    num_wage_2 = 40
    wage_3 = 17
    num_wage_3 = num_employees - num_wage_1 - num_wage_2
    cost = (num_wage_1 * wage_1 + num_wage_2 * wage_2 + num_wage_3 * wage_3) * 8
    result = cost
    return result

print(solution())