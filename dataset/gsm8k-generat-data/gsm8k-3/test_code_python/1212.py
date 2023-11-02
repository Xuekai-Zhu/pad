def solution():
    """Darren bought 4 boxes of crackers. Each box contained 24 crackers. If Calvin bought one box less than twice as many boxes of crackers as Darren, how many crackers did they buy altogether?"""
    # Define the number of boxes and crackers Darren bought
    darren_boxes = 4
    darren_crackers = 24 * darren_boxes

    # Define the number of boxes Calvin bought
    calvin_boxes = 2 * darren_boxes - 1
    calvin_crackers = 24 * calvin_boxes

    # Calculate the total number of crackers
    total_crackers = darren_crackers + calvin_crackers

    # Display the total number of crackers
    result = total_crackers
    return result

print(solution())