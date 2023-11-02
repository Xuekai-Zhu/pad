def solution():
    """Seth and his brother want to see their favorite band in concert.  The tickets are $50.00 each.  There is a 15% processing fee for the tickets.  They are also charged $10.00 for parking and an additional $5.00 per person entrance fee.  How much will it cost to go to the concert?"""
    # Define the variables
    ticket_price = 50
    processing_fee_percent = 0.15
    parking_fee = 10
    entrance_fee_per_person = 5
    number_of_persons = 2

    # Calculate the total ticket cost with processing fee included
    total_ticket_cost = ticket_price * number_of_persons * (1 + processing_fee_percent)

    # Calculate the total cost including ticket cost, parking fee and entrance fee
    total_cost = total_ticket_cost + parking_fee + entrance_fee_per_person * number_of_persons

    # Display the total cost
    result = total_cost
    return result

print(solution())