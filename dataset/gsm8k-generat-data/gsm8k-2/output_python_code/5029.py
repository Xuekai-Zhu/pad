def solution():
    """One ticket to the underground costs $3. In one minute, the metro sells an average of 5 such tickets. What will be the earnings from the tickets in 6 minutes?"""
    ticket_price = 3
    tickets_per_minute = 5
    total_tickets_sold = tickets_per_minute * 6
    total_earnings = total_tickets_sold * ticket_price
    result = total_earnings
    return result

print(solution())