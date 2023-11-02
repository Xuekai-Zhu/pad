def solution():
    """A concert ticket costs $40. Mr. Benson bought 12 tickets and received a 5% discount for every ticket bought that exceeds 10. How much did Mr. Benson pay in all?"""
    ticket_price = 40
    num_tickets = 12
    discount = 0.05
    if num_tickets > 10:
        extra_tickets = num_tickets - 10
        extra_cost = extra_tickets * ticket_price * (1 - discount)
        total_cost = (10 * ticket_price) + extra_cost
    else:
        total_cost = num_tickets * ticket_price
    result = total_cost
    return result

print(solution())