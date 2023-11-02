def solution():
    """Brian's friend Bobby has 5 fewer than 3 times as many video games as Brian does. If Brian has 20 video games but lost 5 right before the comparison was made, how many does Bobby have?"""
    brian_games = 20
    brian_games -= 5
    bobby_games = (3 * brian_games) - 5
    result = bobby_games
    return result

print(solution())