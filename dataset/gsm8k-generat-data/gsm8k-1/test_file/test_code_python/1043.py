def solution():
    """Rory is retrieving tennis balls from the court after a tennis match. In the first of three sets, he had to retrieve four more balls than in the second set. In the third set, he retrieved half as many balls as in the second. He retrieved 19 tennis balls in all. How many tennis balls did he retrieve in the first set of the match?"""
    
    total_balls = 19
    second_set_balls = total_balls / 3  # Since it's the second of three sets
    first_set_balls = second_set_balls + 4  # Four more than the second set
    result = first_set_balls
    
    return result

print(solution())