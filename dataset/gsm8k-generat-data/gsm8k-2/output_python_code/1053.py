def solution():
    """Seth and his brother want to see their favorite band in concert. The tickets are $50.00 each. There is a 15% processing fee for the tickets. They are also charged $10.00 for parking and an additional $5.00 per person entrance fee. How much will it cost to go to the concert?"""
    ticket_price = 50
    processing_fee = ticket_price * 0.15
    parking_fee = 10
    entrance_fee = 5
    num_people = 2
    total_cost = (ticket_price + processing_fee) * num_people + parking_fee + entrance_fee * num_people
    result = total_cost
    return result

print(solution())