def solution():
    """Darren bought 4 boxes of crackers. Each box contained 24 crackers. If Calvin bought one box less than twice as many boxes of crackers as Darren, how many crackers did they buy altogether?"""
    darren_boxes = 4
    darren_crackers = darren_boxes * 24
    calvin_boxes = 2 * darren_boxes - 1
    calvin_crackers = calvin_boxes * 24
    total_crackers = darren_crackers + calvin_crackers
    result = total_crackers
    return result

print(solution())