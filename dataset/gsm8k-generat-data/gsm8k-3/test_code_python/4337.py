def solution():
    """Carrie worked for 2 hours a day for 4 days to make and decorate a wedding cake. She was paid $22 an hour. The cost for supplies to make the cake was $54. How much profit did Carrie earn on the cake?"""
    # Define the number of hours worked and the hourly rate
    hours_worked = 2 * 4
    hourly_rate = 22

    # Calculate Carrie's earnings
    earnings = hours_worked * hourly_rate

    # Calculate the total cost of making the cake
    total_cost = earnings + 54

    # Calculate Carrie's profit
    profit = earnings - 54

    # Display Carrie's profit
    result = profit
    return result

print(solution())