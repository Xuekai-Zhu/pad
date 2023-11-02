def solution():
    
    ticket_price = 50
    processing_fee = ticket_price * 0.15
    parking_fee = 10
    entrance_fee = 5
    num_people = 2
    total_cost = (ticket_price + processing_fee) * num_people + parking_fee + entrance_fee * num_people
    result = total_cost
    return result

print(solution())