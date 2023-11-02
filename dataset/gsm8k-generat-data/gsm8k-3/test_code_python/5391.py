def solution():
    """Reggie is playing marbles with his friend. His friend arrives with 100 marbles. Each game, they bet ten marbles and whoever wins gets to keep all the marbles. After 9 games, Reggie has 90 marbles. How many games has he lost?"""
    # Define the initial number of marbles
    initial_marbles = 100

    # Define the bet per game
    bet_per_game = 10

    # Calculate the number of games played
    total_games = (initial_marbles - 90) / bet_per_game

    # Calculate the number of games lost
    games_lost = total_games - 1

    # Display the number of games lost
    result = games_lost
    return result

print(solution())