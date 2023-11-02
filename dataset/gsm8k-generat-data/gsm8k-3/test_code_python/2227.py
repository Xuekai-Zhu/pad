def solution():
    """Russel and Jen went to the circus. Jen played a shooting game twice, while Russel rode the carousel three times. If the shooting game costs 5 tickets and the carousel costs 3 tickets. How many tickets did they use?"""
    # Define the cost of each game/ride in tickets
    SHOOTING_GAME_COST = 5
    CAROUSEL_COST = 3

    # Define the number of times Jen played the shooting game and Russel rode the carousel
    jen_shooting_game_count = 2
    russel_carousel_count = 3

    # Calculate the total number of tickets used
    total_tickets = jen_shooting_game_count * SHOOTING_GAME_COST + russel_carousel_count * CAROUSEL_COST

    # Display the total number of tickets used
    result = total_tickets
    return result

print(solution())