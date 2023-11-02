def solution():
    """John decides to install a ramp in his house. He needs to get permits which cost $250. After that, he hires a contractor which costs $150 an hour and the guy works for 3 days at 5 hours per day. He also pays an inspector 80% less to make sure it is OK. How much was the total cost?"""
    # Define the cost of permits and the hourly rate of the contractor
    permit_cost = 250
    contractor_rate = 150

    # Calculate the total hours worked by the contractor
    total_hours = 3 * 5

    # Calculate the total cost of the contractor's work
    contractor_cost = total_hours * contractor_rate

    # Calculate the cost of the inspector's work
    inspector_cost = contractor_cost * 0.2

    # Calculate the total cost of the ramp installation
    total_cost = permit_cost + contractor_cost + inspector_cost

    # return the result
    result = total_cost
    return result

print(solution())