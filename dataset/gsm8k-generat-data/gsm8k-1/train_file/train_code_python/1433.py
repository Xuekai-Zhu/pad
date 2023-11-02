def solution():
    """A typical tournament of tennis has 4 rounds. There are 8 games in the first round, 4 in the second round, 2 in the third round and 1 during the finals. If each game requires new tennis balls, and on average each game uses 5 cans of tennis balls, how many tennis balls in total are used at the end of the tournament if each can has 3 tennis balls?"""
    first_round = 8
    second_round = 4
    third_round = 2
    finals = 1
    total_games = first_round + second_round + third_round + finals
    cans_per_game = 5
    balls_per_can = 3
    total_balls = total_games * cans_per_game * balls_per_can
    result = total_balls
    return result

print(solution())