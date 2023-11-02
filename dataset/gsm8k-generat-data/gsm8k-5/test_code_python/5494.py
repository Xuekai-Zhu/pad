def solution():
    adult_ticket_cost = 8
    child_ticket_cost = 3
    adult_budget = 35

    # Calculate the maximum number of children the adult can take to the movies with her budget
    max_children = (adult_budget - adult_ticket_cost) / child_ticket_cost
    result = int(max_children)
    return result

print(solution())