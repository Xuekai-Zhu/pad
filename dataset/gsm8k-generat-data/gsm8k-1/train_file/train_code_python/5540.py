def solution():
    """Five adults and two children go to see a movie and buy $12 worth of concessions. The total cost of their trip is $76. If each child's ticket is $7, how much, in dollars, are the adult tickets?"""
    num_adults = 5
    num_children = 2
    concession_cost = 12
    total_cost = 76
    child_ticket_cost = 7
    total_children_cost = num_children * child_ticket_cost
    adult_ticket_cost = (total_cost - concession_cost - total_children_cost) / num_adults
    result = adult_ticket_cost
    return result

print(solution())