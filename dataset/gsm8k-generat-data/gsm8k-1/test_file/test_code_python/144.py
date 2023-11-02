def solution():
    """Brittany and her mom go to the museum. The cost of admission is $12 for adults and $10 for children. Brittany's mom gives the cashier money for 1 child ticket and 1 adult ticket. If she received $8 in change, how much money, in dollars, did she give the cashier?"""
    adult_ticket_cost = 12
    child_ticket_cost = 10
    total_cost = adult_ticket_cost + child_ticket_cost
    change_received = 8
    amount_paid = total_cost + change_received
    result = amount_paid
    return result

print(solution())