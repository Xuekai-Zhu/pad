def solution():
    """A quarterback steps back to throw 80 times in a game. 30 percent of the time he does not get a pass thrown. Half of the times that he does not throw the ball he is sacked for a loss. How many times is the quarterback sacked for a loss in the game?"""
    # Define the number of times the quarterback steps back to throw
    throws = 80

    # Calculate the number of times the quarterback does not throw the ball
    no_throw = int(throws * 0.3)

    # Calculate the number of times the quarterback is sacked for a loss
    sacked = int(no_throw * 0.5)

    result = sacked
    return result

print(solution())