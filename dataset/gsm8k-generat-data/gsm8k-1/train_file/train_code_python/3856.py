def solution():
    """A quarterback steps back to throw 80 times in a game. 30 percent of the time he does not get a pass thrown. Half of the times that he does not throw the ball he is sacked for a loss. How many times is the quarterback sacked for a loss in the game?"""
    throws = 80
    no_throw_percent = 30
    no_throw = throws * (no_throw_percent / 100)
    sacks = no_throw / 2
    result = sacks
    return result

print(solution())