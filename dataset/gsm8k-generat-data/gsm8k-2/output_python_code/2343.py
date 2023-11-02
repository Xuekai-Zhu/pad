def solution():
    """Olivia's insurance premium starts out at $50/month. It goes up 10% for every accident and $5/month for every ticket. If she gets in one accident and gets 3 tickets, what's her new insurance premium?"""
    base_premium = 50
    accident_increase = 0.1
    ticket_increase = 5
    num_accidents = 1
    num_tickets = 3
    premium = base_premium
    premium += premium * accident_increase * num_accidents
    premium += ticket_increase * num_tickets
    result = premium
    return result

print(solution())