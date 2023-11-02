def solution():
    """Ralph is going to practice playing tennis with a tennis ball machine that shoots out tennis balls for Ralph to hit. He loads up the machine with 175 tennis balls to start with. Out of the first 100 balls, he manages to hit 2/5 of them. Of the next 75 tennis balls, he manages to hit 1/3 of them. Out of all the tennis balls, how many did Ralph not hit?"""
    total_balls = 175
    first_100_hit = int(2/5 * 100)
    next_75_hit = int(1/3 * 75)
    total_hit = first_100_hit + next_75_hit
    not_hit = total_balls - total_hit
    result = not_hit
    return result

print(solution())