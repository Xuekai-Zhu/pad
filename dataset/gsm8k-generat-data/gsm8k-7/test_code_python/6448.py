def solution():
    num_kids = 6
    num_adults = 2
    total_cost = 50

    # Calculate the cost of one adult ticket
    adult_ticket_price = total_cost / (num_kids / 2 + num_adults)

    # Calculate the cost of one kid's ticket
    kid_ticket_price = adult_ticket_price / 2
    result = kid_ticket_price
    return result

print(solution())