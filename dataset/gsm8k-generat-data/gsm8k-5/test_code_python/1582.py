def solution():
    # Calculate the total number of tickets Connie spent
    tickets_koala = (1/2) * total_tickets  # Connie spent half of her total tickets on a stuffed koala bear
    tickets_earbuds = 10  # Connie spent 10 tickets on earbuds
    tickets_glow_bracelets = 15  # Connie spent 15 tickets on glow bracelets
    total_spent = tickets_koala + tickets_earbuds + tickets_glow_bracelets

    # Calculate the total number of tickets Connie redeemed
    total_tickets = 2 * total_spent
    
    result = total_tickets
    return result

print(solution())