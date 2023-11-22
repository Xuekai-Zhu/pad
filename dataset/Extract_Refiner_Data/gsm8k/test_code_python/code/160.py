def solution():
    
    # Define the cost of the accountant
    accountant_cost = 90

    # Calculate the total hours worked
    total_hours = accountant_cost / (35/60)

    # Calculate the net income
    net_income = total_hours * 35

    # Calculate the difference between the net income and the accountant's cost
    difference = net_income - accountant_cost

    # return the result
    result = difference
    return result

print(solution())