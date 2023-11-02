def solution():
    """Connie redeemed all her arcade tickets today. She spent half of them on a stuffed koala bear. She spent 10 tickets on a pair of earbuds. She spent another 15 tickets on glow bracelets. How many tickets did Connie redeem today?"""
    koala_tickets = 0.5 * total_tickets
    earbuds_tickets = 10
    glow_bracelets_tickets = 15
    total_tickets = koala_tickets + earbuds_tickets + glow_bracelets_tickets
    result = total_tickets
    return result

print(solution())