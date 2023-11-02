def solution():
    ticket_cost = 50.00
    processing_fee = ticket_cost * 0.15
    parking_cost = 10.00
    entrance_fee = 5.00
    num_people = 2

    total_cost = (ticket_cost + processing_fee) * num_people + parking_cost + entrance_fee * num_people
    result = total_cost
    return result

print(solution())