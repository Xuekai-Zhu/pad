def solution():
    """One ticket to the underground costs $3. In one minute, the metro sells an average of 5 such tickets. What will be the earnings from the tickets in 6 minutes?"""
    ticket_cost = 3
    tickets_sold_per_minute = 5
    minutes = 6
    tickets_sold = tickets_sold_per_minute * minutes
    earnings = tickets_sold * ticket_cost
    result = earnings
    return result

print(solution())