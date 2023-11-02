def solution():
    """There are one hundred tickets to be sold for a volleyball game. Andrea sold twice as many tickets as Jude while Sandra sold 4 more than half the number of tickets Jude sold. If Jude sold 16 tickets, how many tickets need to be sold?"""
    jude_tickets = 16
    andrea_tickets = jude_tickets * 2
    sandra_tickets = (jude_tickets / 2) + 4
    total_tickets_sold = jude_tickets + andrea_tickets + sandra_tickets
    tickets_left = 100 - total_tickets_sold
    result = tickets_left
    return result

print(solution())