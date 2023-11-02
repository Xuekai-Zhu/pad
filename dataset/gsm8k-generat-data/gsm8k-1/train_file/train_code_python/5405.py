def solution():
    """Mr. and Mrs. Boyden take their 3 children to a leisure park. They buy tickets for the whole family. The cost of an adult ticket is $6 more than the cost of a child ticket. The total cost of the 5 tickets is $77. What is the cost of an adult ticket?"""
    total_tickets = 5
    total_cost = 77
    child_cost = x
    adult_cost = x + 6
    child_tickets = 3
    adult_tickets = total_tickets - child_tickets
    total_cost = (child_tickets * child_cost) + (adult_tickets * adult_cost)
    adult_cost = (total_cost - (child_tickets * child_cost)) / adult_tickets
    result = adult_cost
    return result

print(solution())