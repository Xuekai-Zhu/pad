def solution():
    
    ticket_price = 50
    processing_fee_percent = 15
    processing_fee = ticket_price * (processing_fee_percent / 100)
    total_ticket_price = ticket_price + processing_fee
    parking_fee = 10
    entrance_fee_per_person = 5
    number_of_people = 2  
    total_cost = total_ticket_price * number_of_people + parking_fee + entrance_fee_per_person * number_of_people
    result = total_cost
    return result

print(solution())