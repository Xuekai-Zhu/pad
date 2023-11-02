def solution():
    game_price = 66
    num_movie_tickets = 3
    movie_ticket_price = 12

    # Calculate the total cost of movie tickets
    total_movie_cost = num_movie_tickets * movie_ticket_price

    # Calculate the total cost of entertainment
    total_entertainment_cost = game_price + total_movie_cost
    result = total_entertainment_cost
    return result

print(solution())