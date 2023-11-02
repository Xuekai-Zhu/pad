def solution():
    # Calculate the cost of one football game ticket
    movie_ticket_cost = 30
    movie_to_game_ratio = 2
    game_ticket_cost = movie_ticket_cost / movie_to_game_ratio

    # Calculate the total cost of eight movie tickets
    num_movie_tickets = 8
    total_movie_cost = num_movie_tickets * movie_ticket_cost

    # Calculate the total cost of five football game tickets
    num_game_tickets = 5
    total_game_cost = num_game_tickets * game_ticket_cost

    # Calculate the total amount Chandler will pay
    total_cost = total_movie_cost + total_game_cost
    result = total_cost
    return result

print(solution())