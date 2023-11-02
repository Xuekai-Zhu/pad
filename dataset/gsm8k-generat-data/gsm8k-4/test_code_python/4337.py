def solution():
    """Carrie worked for 2 hours a day for 4 days to make and decorate a wedding cake. She was paid $22 an hour. The cost for supplies to make the cake was $54. How much profit did Carrie earn on the cake?"""
    # Define the number of hours worked and the hourly wage
    hours_worked = 2 * 4
    hourly_wage = 22

    # Calculate the total earnings from the cake
    earnings = hours_worked * hourly_wage

    # Calculate the total cost of supplies
    supply_cost = 54

    # Calculate the profit on the cake
    profit = earnings - supply_cost

    result = profit
    return result

print(solution())