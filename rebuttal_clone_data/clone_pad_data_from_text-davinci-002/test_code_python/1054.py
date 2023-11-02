def solution():
    ticket_price = 50
    processing_fee = 15
    parking_fee = 10
    entrance_fee = 5
    total_fee = (ticket_price * processing_fee / 100) + ticket_price + parking_fee + (2 * entrance_fee)
    result = total_fee
    
    return result

print(solution())