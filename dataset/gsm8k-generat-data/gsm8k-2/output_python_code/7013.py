def solution():
    """Claire was in charge of passing out free balloons to all the children at the fair. She started with 50 balloons. While passing 1 balloon to a little girl, 12 balloons floated away. Over the next thirty minutes, she gave 9 more away and grabbed the last 11 from her coworker. How many balloons does Claire have?"""
    starting_balloons = 50
    lost_balloons = 12
    given_away_balloons = 1 + 9
    coworker_balloons = 11
    total_balloons = starting_balloons - lost_balloons + given_away_balloons + coworker_balloons
    result = total_balloons
    return result

print(solution())