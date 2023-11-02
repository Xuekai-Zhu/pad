def solution():
    ticket_price = 50  # The tickets cost $50 each
    processing_fee = ticket_price * 0.15  # There is a 15% processing fee for the tickets
    parking_fee = 10  # The parking fee is $10
    entrance_fee = 5 * 2  # Seth and his brother each have to pay a $5 entrance fee

    # Calculate the total cost of the tickets
    total_ticket_price = (ticket_price + processing_fee) * 2  

    # Calculate the total cost of going to the concert
    total_cost = total_ticket_price + parking_fee + entrance_fee
    result = total_cost
    return result

print(solution())