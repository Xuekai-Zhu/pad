def solution():
    """A play was held in an auditorium and its ticket costs $10. An auditorium has 20 rows and each row has 10 seats. If only 3/4 of the seats were sold, how much was earned from the play?"""
    # Define the price of a ticket
    ticket_price = 10

    # Calculate the total number of seats in the auditorium
    total_seats = 20 * 10

    # Calculate the number of seats sold
    seats_sold = total_seats * 3/4

    # Calculate the total earnings from the play
    earnings = seats_sold * ticket_price

    # Return the result
    result = earnings
    return result

print(solution())