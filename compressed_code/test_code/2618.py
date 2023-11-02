def solution():
    
    adult_ticket_price = 6
    child_ticket_price = 4
    total_seats = 250
    total_children = 188
    total_adults = total_seats - total_children
    adult_revenue = adult_ticket_price * total_adults
    child_revenue = child_ticket_price * total_children
    total_revenue = adult_revenue + child_revenue
    result = total_revenue
    return result

print(solution())