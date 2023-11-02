def solution():
    """Claire was in charge of passing out free balloons to all the children at the fair.  She started with 50 balloons.  While passing 1 balloon to a little girl, 12 balloons floated away.  Over the next thirty minutes, she gave 9 more away and grabbed the last 11 from her coworker.  How many balloons does Claire have?"""
    # Define the initial number of balloons
    balloons = 50

    # Subtract the balloon given to the little girl and the balloons that floated away
    balloons -= 1
    balloons -= 12

    # Give away 9 more balloons
    balloons -= 9

    # Add the balloons from her coworker
    balloons += 11

    # Return the final number of balloons
    result = balloons
    return result

print(solution())