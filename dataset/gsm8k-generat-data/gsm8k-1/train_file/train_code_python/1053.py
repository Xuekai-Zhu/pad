def solution():
    """Seth and his brother want to see their favorite band in concert. The tickets are $50.00 each. There is a 15% processing fee for the tickets. They are also charged $10.00 for parking and an additional $5.00 per person entrance fee. How much will it cost to go to the concert?"""
    ticket_price = 50
    processing_fee_percent = 15
    processing_fee = ticket_price * (processing_fee_percent / 100)
    total_ticket_price = ticket_price + processing_fee
    parking_fee = 10
    entrance_fee_per_person = 5
    number_of_people = 2  # Seth and his brother
    total_cost = total_ticket_price * number_of_people + parking_fee + entrance_fee_per_person * number_of_people
    result = total_cost
    return result

print(solution())