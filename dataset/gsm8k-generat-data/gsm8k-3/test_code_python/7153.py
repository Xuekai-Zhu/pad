def solution():
    """Mark needs to replace the radiator in his car.  The work takes 2 hours and the mechanic charges $75 an hour.  The part cost $150.  How much did he pay?"""
    # Define the cost of the part
    PART_COST = 150

    # Define the number of hours of labor required
    labor_hours = 2

    # Define the hourly rate of the mechanic
    labor_rate = 75

    # Calculate the total cost of labor
    labor_cost = labor_hours * labor_rate

    # Calculate the total cost of the repair
    total_cost = PART_COST + labor_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())