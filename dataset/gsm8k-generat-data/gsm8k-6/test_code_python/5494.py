def solution():
    # Calculate the maximum number of children the adult can take to the movies
    budget = 35
    adult_ticket = 8
    child_ticket = 3
    max_children = (budget - adult_ticket) // child_ticket

    result = max_children
    return result

print(solution())