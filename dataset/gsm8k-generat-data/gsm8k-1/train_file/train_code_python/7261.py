def solution():
    """Sebastian bought art exhibit tickets for his parents and himself. Tickets were $44 per person. He was also charged an $18 service fee for the online transaction. What is the total amount he paid for the tickets?"""
    num_people = 3
    ticket_cost = 44
    service_fee = 18
    total_cost = num_people * ticket_cost + service_fee
    result = total_cost
    return result

print(solution())