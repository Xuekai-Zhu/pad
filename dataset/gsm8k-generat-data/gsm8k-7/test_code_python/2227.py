def solution():
    num_shooting_games = 2
    shooting_game_cost = 5

    num_carousel_rides = 3
    carousel_cost = 3

    # Calculate the cost of all shooting games
    total_shooting_cost = num_shooting_games * shooting_game_cost

    # Calculate the cost of all carousel rides
    total_carousel_cost = num_carousel_rides * carousel_cost

    # Calculate the total number of tickets used
    total_tickets_used = total_shooting_cost + total_carousel_cost
    result = total_tickets_used
    return result

print(solution())