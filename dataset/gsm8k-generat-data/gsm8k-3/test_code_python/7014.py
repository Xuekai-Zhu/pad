def solution():
    """Claire was in charge of passing out free balloons to all the children at the fair.  She started with 50 balloons.  While passing 1 balloon to a little girl, 12 balloons floated away.  Over the next thirty minutes, she gave 9 more away and grabbed the last 11 from her coworker.  How many balloons does Claire have?"""
    # Define the initial number of balloons and the number of balloons lost
    initial_balloons = 50
    lost_balloons = 12

    # Calculate the number of balloons Claire has after giving one away and losing some
    balloons = initial_balloons - 1 - lost_balloons

    # Give away some more balloons
    balloons -= 9

    # Get some more balloons from her coworker
    balloons += 11

    # Display the total number of balloons Claire has
    result = balloons
    return result

print(solution())