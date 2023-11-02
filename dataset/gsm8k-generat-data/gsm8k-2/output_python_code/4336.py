def solution():
    """Carrie worked for 2 hours a day for 4 days to make and decorate a wedding cake.
    She was paid $22 an hour. The cost for supplies to make the cake was $54.
    How much profit did Carrie earn on the cake?"""
    hours_worked = 2 * 4
    hourly_wage = 22
    labor_cost = hours_worked * hourly_wage
    supply_cost = 54
    total_cost = labor_cost + supply_cost
    revenue = 150  # assuming she charged $150 for the cake
    profit = revenue - total_cost
    result = profit
    return result

print(solution())