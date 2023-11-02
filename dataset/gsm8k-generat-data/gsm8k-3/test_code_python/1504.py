def solution():
    """A small theater company sells tickets to a show. They have a 400 seat theater and fill to 80% capacity. Each ticket cost $30. They repeated the same performance 2 other days. How much did they make?"""
    # Define the theater capacity, ticket price, and number of showings
    THEATER_CAPACITY = 400
    TICKET_PRICE = 30
    NUM_SHOWINGS = 3

    # Calculate the number of tickets sold for each showing
    tickets_sold = int(THEATER_CAPACITY * 0.8)

    # Calculate the total revenue from all showings
    total_revenue = tickets_sold * TICKET_PRICE * NUM_SHOWINGS

    # Display the total revenue
    result = total_revenue
    return result

print(solution())