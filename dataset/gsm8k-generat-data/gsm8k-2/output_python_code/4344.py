def solution():
    """A family went out to see a movie. The regular ticket costs $9 and the ticket for children is $2 less. They gave the cashier two $20 bills and they received a $1 change. How many children are there if there are 2 adults in the family?"""
    adult_tickets = 2
    adult_ticket_price = 9
    child_ticket_price = adult_ticket_price - 2
    total_ticket_price = (adult_tickets * adult_ticket_price) + (child_tickets * child_ticket_price)
    change = 1
    total_cost = total_ticket_price + change
    paid = 20 * 2
    remaining = paid - total_cost
    child_tickets = remaining / child_ticket_price
    result = child_tickets
    return result

print(solution())