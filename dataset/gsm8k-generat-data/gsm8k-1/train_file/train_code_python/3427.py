def solution():
    """Jorge bought 24 tickets for $7 each. For purchasing so many, he is given a discount of 50%. How much, in dollars, did he spend on tickets?"""
    num_tickets = 24
    ticket_cost = 7
    discount_percent = 50
    discount_amount = (num_tickets * ticket_cost) * (discount_percent / 100)
    total_cost = (num_tickets * ticket_cost) - discount_amount
    result = total_cost
    return result

print(solution())