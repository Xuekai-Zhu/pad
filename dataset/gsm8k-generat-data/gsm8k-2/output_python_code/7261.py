def solution():
    """Sebastian bought art exhibit tickets for his parents and himself. Tickets were $44 per person. He was also charged an $18 service fee for the online transaction. What is the total amount he paid for the tickets?"""
    num_tickets = 3
    ticket_price = 44
    service_fee = 18
    total_price = num_tickets * ticket_price + service_fee
    result = total_price
    return result

print(solution())