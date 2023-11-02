def solution():
    """Mary goes with her 3 children to the circus. Tickets cost $2 for adults and $1 for children. Mary pays with a $20 bill. How much change will she receive?"""
    num_adults = 1
    num_children = 3
    adult_ticket_price = 2
    child_ticket_price = 1
    total_cost = num_adults * adult_ticket_price + num_children * child_ticket_price
    change = 20 - total_cost
    result = change
    return result

print(solution())