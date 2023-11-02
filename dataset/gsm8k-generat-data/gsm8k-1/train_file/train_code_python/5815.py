def solution():
    """If eight movie tickets cost 2 times as much as one football game ticket, and each movie ticket is sold at $30, calculate the total amount of money Chandler will pay if he buys eight movie tickets and five football game tickets."""
    movie_tickets = 8
    football_tickets = 5
    movie_ticket_price = 30
    football_ticket_price = movie_ticket_price / 2
    total_cost = (movie_tickets * movie_ticket_price) + (football_tickets * football_ticket_price)
    result = total_cost
    return result

print(solution())