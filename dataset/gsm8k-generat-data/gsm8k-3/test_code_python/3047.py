def solution():
    """A play was held in an auditorium and its ticket costs $10. An auditorium has 20 rows and each row has 10 seats. If only 3/4 of the seats were sold, how much was earned from the play?"""
    # Define the ticket price
    TICKET_PRICE = 10

    # Define the number of rows and seats per row
    ROWS = 20
    SEATS_PER_ROW = 10

    # Calculate the total number of seats in the auditorium
    total_seats = ROWS * SEATS_PER_ROW

    # Calculate the number of seats that were sold
    seats_sold = int(total_seats * 0.75)

    # Calculate the total earnings from the play
    earnings = seats_sold * TICKET_PRICE

    # Display the total earnings
    result = earnings
    return result

print(solution())