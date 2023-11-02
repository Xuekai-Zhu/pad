def solution():
    """Claire was in charge of passing out free balloons to all the children at the fair. She started with 50 balloons. While passing 1 balloon to a little girl, 12 balloons floated away. Over the next thirty minutes, she gave 9 more away and grabbed the last 11 from her coworker. How many balloons does Claire have?"""
    starting_balloons = 50
    balloons_lost = 12
    balloons_given_away = 1 + 9
    balloons_received = 11
    current_balloons = starting_balloons - balloons_lost - balloons_given_away + balloons_received
    result = current_balloons
    return result

print(solution())