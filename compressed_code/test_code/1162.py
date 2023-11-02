def solution():
    
    total_seats = 400
    capacity_percentage = 0.8
    filled_seats = total_seats * capacity_percentage
    ticket_price = 30
    total_revenue = filled_seats * ticket_price * 3
    result = total_revenue
    return result

print(solution())