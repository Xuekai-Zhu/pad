def solution():
    adult_ticket_price = 12
    child_ticket_price = 8
    num_popcorns = 2
    popcorn_price = 3

    # Calculate the total cost of adult tickets
    adult_ticket_cost = adult_ticket_price * num_popcorns

    # Calculate the total cost of child tickets
    child_ticket_cost = child_ticket_price * num_popcorns

    # Calculate the total cost of all tickets
    total_cost = adult_ticket_cost + child_ticket_cost
    result = total_cost
    return result

print(solution())