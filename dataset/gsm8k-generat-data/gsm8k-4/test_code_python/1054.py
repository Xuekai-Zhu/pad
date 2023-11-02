def solution():
    """Seth and his brother want to see their favorite band in concert. The tickets are $50.00 each. There is a 15% processing fee for the tickets. They are also charged $10.00 for parking and an additional $5.00 per person entrance fee. How much will it cost to go to the concert?"""
    # Define the cost of the tickets and the processing fee
    ticket_price = 50
    processing_fee = ticket_price * 0.15

    # Calculate the total cost of the tickets
    total_ticket_cost = (ticket_price + processing_fee) * 2

    # Define the cost of parking and the entrance fee
    parking_cost = 10
    entrance_fee = 5 * 2

    # Calculate the total cost of going to the concert
    total_cost = total_ticket_cost + parking_cost + entrance_fee

    # return the result
    result = total_cost
    return result

print(solution())