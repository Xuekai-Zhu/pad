def solution():
    """Mark spent 220 dollars to fix his car.  It needed two parts that cost 20 dollars each, and labor cost .5 dollars a minute. How many hours did the mechanic work?"""
    # Define the cost of the two parts
    part_cost = 20 * 2

    # Calculate the amount spent on labor
    labor_cost = 220 - part_cost

    # Convert the labor cost to minutes
    labor_minutes = labor_cost / 0.5

    # Convert the labor minutes to hours
    labor_hours = labor_minutes / 60

    # Display the number of hours worked by the mechanic
    result = labor_hours
    return result

print(solution())