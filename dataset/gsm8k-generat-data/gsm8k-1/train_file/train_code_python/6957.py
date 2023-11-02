def solution():
    """Together, Alan and Marcy handed out 150 parking tickets. If Marcy handed out 6 fewer than 5 times as many tickets as Alan, how many tickets did Alan hand out?"""
    marcy_tickets = (5 * alan_tickets) - 6
    total_tickets = 150
    # total_tickets = alan_tickets + marcy_tickets
    # Simplify equation using substitution
    alan_tickets = (total_tickets + 6) / 6
    result = alan_tickets
    return result

print(solution())