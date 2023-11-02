def solution():
    """Russel and Jen went to the circus. Jen played a shooting game twice, while Russel rode the carousel three times. If the shooting game costs 5 tickets and the carousel costs 3 tickets. How many tickets did they use?"""
    jen_shooting_game = 2
    russel_carousel = 3
    shooting_game_cost = 5
    carousel_cost = 3
    total_tickets = jen_shooting_game * shooting_game_cost + russel_carousel * carousel_cost
    result = total_tickets
    return result

print(solution())