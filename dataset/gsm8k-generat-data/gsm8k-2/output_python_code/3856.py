def solution():
    """A quarterback steps back to throw 80 times in a game. 30 percent of the time he does not get a pass thrown. Half of the times that he does not throw the ball he is sacked for a loss. How many times is the quarterback sacked for a loss in the game?"""
    total_pass_attempts = 80
    no_pass_attempts = total_pass_attempts * 0.3
    sacks = no_pass_attempts * 0.5
    result = sacks
    return result

print(solution())