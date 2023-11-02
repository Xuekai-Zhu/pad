def solution():
    entrance_ticket = 5
    ticket_for_attraction_kids = 2
    ticket_for_attraction_parents = 4
    number_of_kids = 4
    number_of_parents = 2
    number_of_grandmothers = 1
    total_cost = entrance_ticket + (ticket_for_attraction_kids * number_of_kids) + (ticket_for_attraction_parents * number_of_parents)
    result = total_cost
    return result

print(solution())