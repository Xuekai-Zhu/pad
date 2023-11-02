def solution():
    """Mark spent 220 dollars to fix his car. It needed two parts that cost 20 dollars each, and labor cost .5 dollars a minute. How many hours did the mechanic work?"""
    # Calculate the cost of the two parts
    parts_cost = 20 * 2

    # Calculate the labor cost
    labor_cost = 220 - parts_cost

    # Calculate the number of minutes of labor
    labor_minutes = labor_cost / 0.5

    # Convert minutes to hours
    labor_hours = labor_minutes / 60

    # return the result
    result = labor_hours
    return result

print(solution())