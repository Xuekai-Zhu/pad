def solution():
    """Five adults and two children go to see a movie and buy $12 worth of concessions. The total cost of their trip is $76. If each child's ticket is $7, how much, in dollars, are the adult tickets?"""
    # Define the number of adults, children, and the cost of concessions
    num_adults = 5
    num_children = 2
    concessions_cost = 12

    # Define the cost of each child's ticket
    child_ticket_cost = 7

    # Find the total cost of tickets
    total_cost = 76 - concessions_cost
    total_child_cost = num_children * child_ticket_cost

    # Find the total cost of adult tickets
    adult_ticket_cost = (total_cost - total_child_cost) / num_adults
    result = adult_ticket_cost
    return result

print(solution())