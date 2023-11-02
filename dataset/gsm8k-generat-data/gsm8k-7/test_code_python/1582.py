def solution():
    koala_tickets = None
    earbuds_tickets = 10
    glow_bracelets_tickets = 15

    # Calculate the total number of tickets Connie spent on earbuds and glow bracelets
    total_other_tickets = earbuds_tickets + glow_bracelets_tickets

    # Calculate the total number of tickets Connie spent on the stuffed koala bear
    koala_tickets = total_other_tickets * 2

    # Calculate the total number of tickets Connie redeemed today
    total_tickets = koala_tickets + total_other_tickets
    result = total_tickets
    return result

print(solution())