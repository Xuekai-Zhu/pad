def solution():
    """A small theater company sells tickets to a show. They have a 400 seat theater and fill to 80% capacity. Each ticket cost $30. They repeated the same performance 2 other days. How much did they make?"""
    # Define the seating capacity and ticket price
    seating_capacity = 400
    ticket_price = 30

    # Calculate the number of seats sold for one show
    seats_sold = seating_capacity * 0.8

    # Calculate the total earnings for one show
    earnings_one_show = seats_sold * ticket_price

    # Calculate the total earnings for three shows
    earnings_three_shows = earnings_one_show * 3

    result = earnings_three_shows
    return result

print(solution())