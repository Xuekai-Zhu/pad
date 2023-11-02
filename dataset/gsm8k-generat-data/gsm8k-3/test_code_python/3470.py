def solution():
    """John's car needs a new engine.  The labor costs $75 an hour for 16 hours.  The part itself cost $1200.  How much did the repairs cost in total?"""
    # Define the cost of labor per hour and the number of hours of labor
    LABOR_COST = 75
    LABOR_HOURS = 16

    # Define the cost of the part
    PART_COST = 1200

    # Calculate the total cost of the repairs
    total_cost = (LABOR_COST * LABOR_HOURS) + PART_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())