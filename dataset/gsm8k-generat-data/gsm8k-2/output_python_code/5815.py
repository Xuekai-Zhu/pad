def solution():
    """If eight movie tickets cost 2 times as much as one football game ticket, and each movie ticket is sold at $30, calculate the total amount of money Chandler will pay if he buys eight movie tickets and five football game tickets."""
    movie_ticket_price = 30
    football_ticket_price = movie_ticket_price / 2
    num_movie_tickets = 8
    num_football_tickets = 5
    total_movie_cost = movie_ticket_price * num_movie_tickets
    total_football_cost = football_ticket_price * num_football_tickets
    total_cost = total_movie_cost + total_football_cost
    result = total_cost
    return result

print(solution())