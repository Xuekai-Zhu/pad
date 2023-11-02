def solution():
    """Reggie is playing marbles with his friend. His friend arrives with 100 marbles. Each game, they bet ten marbles and whoever wins gets to keep all the marbles. After 9 games, Reggie has 90 marbles. How many games has he lost?"""
    starting_marbles = 100
    marble_bet = 10
    games_played = 9
    reggie_marbles = 90
    total_marbles_bet = games_played * marble_bet
    marbles_won = total_marbles_bet - (starting_marbles - reggie_marbles)
    games_lost = marbles_won // marble_bet
    result = games_played - games_lost
    return result

print(solution())