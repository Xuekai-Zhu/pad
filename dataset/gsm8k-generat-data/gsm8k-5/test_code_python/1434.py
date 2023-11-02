def solution():
    # Calculate the total number of games in the tournament
    total_games = 8 + 4 + 2 + 1

    # Calculate the total number of cans needed for the tournament
    total_cans = total_games * 5

    # Calculate the total number of tennis balls needed for the tournament
    total_balls = total_cans * 3

    result = total_balls
    return result

print(solution())