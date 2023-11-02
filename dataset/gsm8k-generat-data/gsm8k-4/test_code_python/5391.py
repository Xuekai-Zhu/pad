def solution():
    """Reggie is playing marbles with his friend. His friend arrives with 100 marbles. Each game, they bet ten marbles and whoever wins gets to keep all the marbles. After 9 games, Reggie has 90 marbles. How many games has he lost?"""
    # Define the total number of games played
    total_games = 9

    # Define the starting number of marbles
    starting_marbles = 100

    # Define the number of marbles bet per game
    bet_per_game = 10

    # Calculate the total number of marbles bet in all the games
    total_bet = total_games * bet_per_game

    # Calculate the number of marbles won by Reggie
    reggie_won = starting_marbles - 90

    # Calculate the number of marbles lost by Reggie
    reggie_lost = total_bet - reggie_won

    # Calculate the number of games lost by Reggie
    games_lost = reggie_lost / bet_per_game

    # return the result
    result = games_lost
    return result

print(solution())