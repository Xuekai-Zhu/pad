def solution():
    num_children = 4
    num_parents = 2
    num_grandparents = 1
    entrance_ticket_cost = 5
    child_ticket_cost = 2
    parent_ticket_cost = 4

    # Calculate the total cost of attractions for children
    children_attraction_cost = num_children * child_ticket_cost

    # Calculate the total cost of attractions for parents
    parents_attraction_cost = num_parents * parent_ticket_cost

    # Calculate the total cost of all tickets
    total_ticket_cost = entrance_ticket_cost + children_attraction_cost + parents_attraction_cost

    # Add grandmother's entrance ticket cost
    total_cost = total_ticket_cost + entrance_ticket_cost
    result = total_cost
    return result

print(solution())