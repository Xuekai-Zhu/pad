def solution():
    """Reggie is playing marbles with his friend. His friend arrives with 100 marbles. Each game, they bet ten marbles and whoever wins gets to keep all the marbles. After 9 games, Reggie has 90 marbles. How many games has he lost?"""
    marbles_at_start = 100
    marbles_per_game = 10
    games_played = 9
    marbles_won = marbles_at_start - 90
    games_lost = marbles_won // marbles_per_game
    result = games_lost
    return result

print(solution())