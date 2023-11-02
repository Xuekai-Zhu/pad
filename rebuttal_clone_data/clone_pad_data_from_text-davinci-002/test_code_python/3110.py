def solution():
    adult_ticket = 11
    child_ticket = 8
    senior_ticket = 9
    number_of_adults = 2
    number_of_children = 3
    number_of_seniors = 2
    total_cost = (number_of_adults * adult_ticket) + (number_of_children * child_ticket) + (number_of_seniors * senior_ticket)
    result = total_cost
    return result

print(solution())