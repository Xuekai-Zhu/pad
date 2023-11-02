def solution():
    movie_ticket_price = 30  # Each movie ticket costs $30
    football_ticket_price = movie_ticket_price / 2  # Eight movie tickets cost 2 times the price of one football game ticket
    num_movie_tickets = 8  # Chandler is buying 8 movie tickets
    num_football_tickets = 5  # Chandler is buying 5 football game tickets

    # Calculate the total cost of the movie tickets
    total_movie_cost = movie_ticket_price * num_movie_tickets

    # Calculate the total cost of the football game tickets
    total_football_cost = football_ticket_price * num_football_tickets

    # Calculate the overall total cost
    total_cost = total_movie_cost + total_football_cost
    result = total_cost
    return result

print(solution())