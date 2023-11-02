def solution():
    """In a factory, there are 300 employees. 200 of them earn $12 per hour. Of the rest, 40 of them earn $14 per hour. All others earn $17 per hour. What is the cost to employ all these people for one 8-hour long shift?"""
    num_emp = 300
    rate_1 = 12
    rate_2 = 14
    rate_3 = 17
    num_emp_rate_1 = 200
    num_emp_rate_2 = 40
    num_emp_rate_3 = num_emp - num_emp_rate_1 - num_emp_rate_2

    cost_rate_1 = num_emp_rate_1 * rate_1 * 8
    cost_rate_2 = num_emp_rate_2 * rate_2 * 8
    cost_rate_3 = num_emp_rate_3 * rate_3 * 8

    total_cost = cost_rate_1 + cost_rate_2 + cost_rate_3
    result = total_cost
    return result

print(solution())