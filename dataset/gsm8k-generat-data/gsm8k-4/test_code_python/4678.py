def solution():
    """A show debut and 200 people buy tickets.  For the second showing three times as many people show up.  If each ticket cost $25 how much did the show make?"""
    # Define the number of tickets sold and the ticket price
    tickets_sold = 200
    ticket_price = 25

    # Calculate the total revenue from the first showing
    first_showing_revenue = tickets_sold * ticket_price

    # Calculate the number of people attending the second showing
    second_showing_attendance = tickets_sold * 3

    # Calculate the total revenue from the second showing
    second_showing_revenue = second_showing_attendance * ticket_price

    # Calculate the total revenue from both showings
    total_revenue = first_showing_revenue + second_showing_revenue

    # Return the result
    result = total_revenue
    return result

print(solution())