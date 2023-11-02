def solution():
    
    ticket_cost = 3
    tickets_sold_per_minute = 5
    minutes = 6
    tickets_sold = tickets_sold_per_minute * minutes
    earnings = tickets_sold * ticket_cost
    result = earnings
    return result

print(solution())