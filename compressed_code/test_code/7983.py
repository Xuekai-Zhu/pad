def solution():
    
    goal_tickets = 200
    tickets_first_half = 15 * 8
    tickets_left = goal_tickets - tickets_first_half
    days_left = 31 - 15
    tickets_per_day = tickets_left / days_left
    result = tickets_per_day
    return result

print(solution())