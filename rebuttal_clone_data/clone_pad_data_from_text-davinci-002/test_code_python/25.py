def solution():
    """Ralph is going to practice playing tennis with a tennis ball machine that shoots out tennis balls for Ralph to hit. He loads up the machine with 175 tennis balls to start with. Out of the first 100 balls, he manages to hit 2/5 of them. Of the next 75 tennis balls, he manages to hit 1/3 of them. Out of all the tennis balls, how many did Ralph not hit?"""
    total_balls = 175
    balls_hit = ((2 / 5) * 100) + ((1 / 3) * 75)
    balls_missed = total_balls - balls_hit
    result = balls_missed
    return result

print(solution())