def solution():
    """A movie theater can hold 50 people at a time.  They charge $8.00 a ticket.  On a Tuesday night they only sold 24 tickets.  By not selling out, how much money did they lose?"""
    # Define the capacity of the movie theater and the price per ticket
    THEATER_CAPACITY = 50
    TICKET_PRICE = 8

    # Get the number of tickets sold on Tuesday night
    tickets_sold = 24

    # Calculate the revenue that the movie theater missed out on
    missed_revenue = (THEATER_CAPACITY - tickets_sold) * TICKET_PRICE

    # Display the missed revenue
    result = missed_revenue
    return result

print(solution())