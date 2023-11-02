def solution():
    # Calculate the cost of one football game ticket
    movie_ticket_cost = 30  # given that each movie ticket is sold at $30
    movie_ticket_count = 8  # given that Chandler buys 8 movie tickets
    football_ticket_cost = movie_ticket_cost / 2  # given that 8 movie tickets cost 2 times as much as 1 football game ticket
    football_ticket_count = 5  # given that Chandler buys 5 football game tickets

    # Calculate the total amount paid by Chandler
    total_amount_paid = (movie_ticket_cost * movie_ticket_count) + (football_ticket_cost * football_ticket_count)
    result = total_amount_paid
    return result

print(solution())