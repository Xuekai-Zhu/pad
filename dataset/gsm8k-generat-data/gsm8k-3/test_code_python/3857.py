def solution():
    """A quarterback steps back to throw 80 times in a game.  30 percent of the time he does not get a pass thrown.  Half of the times that he does not throw the ball he is sacked for a loss.  How many times is the quarterback sacked for a loss in the game?"""
    # Define the number of throws and the percentage of throws where no pass is thrown
    throws = 80
    no_pass_percentage = 0.3

    # Calculate the number of times the quarterback does not throw a pass
    no_passes = throws * no_pass_percentage

    # Calculate the number of times the quarterback is sacked for a loss
    sacks = no_passes / 2

    # Display the number of times the quarterback is sacked for a loss
    result = sacks
    return result

print(solution())