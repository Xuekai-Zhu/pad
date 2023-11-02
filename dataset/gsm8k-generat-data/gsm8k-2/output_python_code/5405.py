def solution():
    """Mr. and Mrs. Boyden take their 3 children to a leisure park. They buy tickets for the whole family. The cost of an adult ticket is $6 more than the cost of a child ticket. The total cost of the 5 tickets is $77. What is the cost of an adult ticket?"""
    total_tickets = 5
    total_cost = 77
    child_cost = (total_cost - total_tickets * x) / 3
    adult_cost = child_cost + 6
    result = adult_cost
    return result

print(solution())