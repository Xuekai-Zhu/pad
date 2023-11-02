def solution():
    """A typical tournament of tennis has 4 rounds. There are 8 games in the first round, 4 in the second round, 2 in the third round and 1 during the finals. If each game requires new tennis balls, and on average each game uses 5 cans of tennis balls, how many tennis balls in total are used at the end of the tournament if each can has 3 tennis balls?"""
    # Define the number of games in each round
    round_1_games = 8
    round_2_games = 4
    round_3_games = 2
    finals_games = 1

    # Define the number of cans of tennis balls used per game
    cans_per_game = 5

    # Define the number of balls per can
    balls_per_can = 3

    # Calculate the total number of games
    total_games = round_1_games + round_2_games + round_3_games + finals_games

    # Calculate the total number of cans of tennis balls used
    total_cans = total_games * cans_per_game

    # Calculate the total number of tennis balls used
    total_balls = total_cans * balls_per_can

    # Display the total number of tennis balls used
    result = total_balls
    return result

print(solution())