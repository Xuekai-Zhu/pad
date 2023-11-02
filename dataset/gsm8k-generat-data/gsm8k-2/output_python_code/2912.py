def solution():
    """There are one hundred tickets to be sold for a volleyball game. Andrea sold twice as many tickets as Jude while Sandra sold 4 more than half the number of tickets Jude sold. If Jude sold 16 tickets, how many tickets need to be sold?"""
    jude_tickets = 16
    andrea_tickets = 2 * jude_tickets
    sandra_tickets = 4 + (0.5 * jude_tickets)
    total_tickets = jude_tickets + andrea_tickets + sandra_tickets
    remaining_tickets = 100 - total_tickets
    result = remaining_tickets
    return result

print(solution())