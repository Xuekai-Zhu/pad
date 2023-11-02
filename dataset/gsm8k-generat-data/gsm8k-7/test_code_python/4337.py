def solution():
    hours_worked = 2
    num_days = 4
    wage_per_hour = 22
    cost_of_supplies = 54

    # Calculate the total number of hours worked by Carrie
    total_hours_worked = hours_worked * num_days

    # Calculate the total wage earned by Carrie
    total_wage = total_hours_worked * wage_per_hour

    # Calculate the total profit earned by Carrie
    total_profit = total_wage - cost_of_supplies
    result = total_profit
    return result

print(solution())