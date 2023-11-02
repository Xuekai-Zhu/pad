def solution():
    movie_ticket_price = 30  # in dollars
    football_price = movie_ticket_price / 2

    num_movie_tickets = 8
    num_football_tickets = 5

    # Calculate the total cost of movie tickets
    total_movie_cost = num_movie_tickets * movie_ticket_price

    # Calculate the total cost of football tickets
    total_football_cost = num_football_tickets * football_price

    # Calculate the total cost of all tickets
    total_cost = total_movie_cost + total_football_cost
    result = total_cost
    return result

print(solution())