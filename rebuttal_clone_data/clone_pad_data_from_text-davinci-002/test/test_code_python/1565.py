def solution():
    total_tickets = 200
    tickets_given = 15
    daily_average = 8
    remaining_days = 31 - tickets_given
    remaining_tickets = total_tickets - (tickets_given * daily_average)
    daily_average_needed = remaining_tickets / remaining_days
    
    return daily_average_needed

print(solution())