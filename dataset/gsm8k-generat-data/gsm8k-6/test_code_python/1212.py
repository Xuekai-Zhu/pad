def solution():
    # Calculate the total number of crackers that Darren bought
    darren_boxes = 4
    darren_crackers = 24 * darren_boxes

    # Calculate the number of boxes that Calvin bought
    calvin_boxes = (2 * darren_boxes) - 1

    # Calculate the total number of crackers that Calvin bought
    calvin_crackers = 24 * calvin_boxes

    # Calculate the total number of crackers they bought altogether
    total_crackers = darren_crackers + calvin_crackers
    result = total_crackers
    return result

print(solution())