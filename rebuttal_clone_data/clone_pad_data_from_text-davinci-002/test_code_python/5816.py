def solution():
    total_tickets = 8 + 5
    movie_tickets = 8
    game_tickets = 5
    movie_ticket_cost = movie_tickets * 30
    game_ticket_cost = game_tickets * (movie_ticket_cost / 2)
    total_cost = movie_ticket_cost + game_ticket_cost
    result = total_cost
    return result

print(solution())