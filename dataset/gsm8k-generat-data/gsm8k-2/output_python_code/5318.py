def solution():
    """400 adults and 200 children go to a Broadway show. The price of an adult ticket is twice that of a child's ticket. What is the price of an adult ticket if the total amount collected is $16,000?"""
    total_people = 400 + 200
    total_amount = 16000
    child_ticket_price = x
    adult_ticket_price = 2 * child_ticket_price
    total_tickets_sold = 400 + 200
    total_amount_collected = 400 * adult_ticket_price + 200 * child_ticket_price
    while total_amount_collected != total_amount:
        adult_ticket_price += 0.01
        child_ticket_price = adult_ticket_price / 2
        total_amount_collected = 400 * adult_ticket_price + 200 * child_ticket_price

    result = adult_ticket_price
    return result

print(solution())