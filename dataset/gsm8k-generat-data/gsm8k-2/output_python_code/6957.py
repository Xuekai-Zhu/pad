def solution():
    """Together, Alan and Marcy handed out 150 parking tickets. If Marcy handed out 6 fewer than 5 times as many tickets as Alan, how many tickets did Alan hand out?"""
    total_tickets = 150
    marcy_tickets = (5 * alan_tickets) - 6
    alan_tickets = (total_tickets - marcy_tickets)
    result = alan_tickets
    return result

print(solution())