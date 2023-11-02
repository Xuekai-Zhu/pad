def solution():
    """John decides to install a ramp in his house. He needs to get permits which cost $250. After that, he hires a contractor which costs $150 an hour and the guy works for 3 days at 5 hours per day. He also pays an inspector 80% less to make sure it is OK. How much was the total cost?"""
    permit_cost = 250
    contractor_cost = 150 * 5 * 3
    inspector_cost = 0.2 * contractor_cost
    total_cost = permit_cost + contractor_cost + inspector_cost
    result = total_cost
    return result

print(solution())