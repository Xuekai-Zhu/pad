def solution():
    """John decides to install a ramp in his house.  He needs to get permits which cost $250.  After that, he hires a contractor which costs $150 an hour and the guy works for 3 days at 5 hours per day.  He also pays an inspector 80% less to make sure it is OK.  How much was the total cost?"""
    # Define the cost of the permits and the hourly rate of the contractor
    permit_cost = 250
    contractor_rate = 150

    # Calculate the cost of the contractor's work
    contractor_hours = 3 * 5
    contractor_cost = contractor_hours * contractor_rate

    # Calculate the cost of the inspector's work
    inspector_discount = 0.8
    inspector_cost = contractor_cost * inspector_discount

    # Calculate the total cost
    total_cost = permit_cost + contractor_cost + inspector_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())