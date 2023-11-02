def solution():
    
    weekly_visits = 1
    performance_time = 3
    ticket_price = 5
    total_cost = 0
    for i in range(6):
        total_cost += weekly_visits * performance_time * ticket_price
    result = total_cost
    return result

print(solution())