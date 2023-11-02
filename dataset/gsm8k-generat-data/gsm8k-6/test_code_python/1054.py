def solution():
    # Calculate the total cost to see the favorite band in concert
    ticket_price = 50  # price of one ticket
    num_tickets = 2  # two people are going to the concert
    processing_fee = 0.15 * ticket_price * num_tickets  # 15% processing fee for the tickets
    parking_fee = 10  # $10.00 for parking
    entrance_fee = 5 * num_tickets  # $5.00 per person entrance fee
    total_cost = ticket_price*num_tickets + processing_fee + parking_fee + entrance_fee
    result = total_cost
    return result

print(solution())