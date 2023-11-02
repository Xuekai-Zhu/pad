def solution():
    """A movie theater can hold 50 people at a time. They charge $8.00 a ticket. On a Tuesday night they only sold 24 tickets. By not selling out, how much money did they lose?"""
    # Define the capacity of the theater and the ticket price
    THEATER_CAPACITY = 50
    TICKET_PRICE = 8.00

    # Define the number of tickets sold on Tuesday night
    tickets_sold = 24

    # Calculate the potential revenue if the theater had sold out
    potential_revenue = THEATER_CAPACITY * TICKET_PRICE

    # Calculate the actual revenue from tickets sold on Tuesday
    actual_revenue = tickets_sold * TICKET_PRICE

    # Calculate the lost revenue by not selling out
    lost_revenue = potential_revenue - actual_revenue

    result = lost_revenue
    return result

print(solution())