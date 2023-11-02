def solution():
    # Calculate how many boxes of crackers Calvin bought
    calvin_boxes = 2 * 4 - 1

    # Calculate the total number of crackers Darren bought
    darren_total = 4 * 24

    # Calculate the total number of crackers Calvin bought
    calvin_total = calvin_boxes * 24

    # Calculate the total number of crackers they bought altogether
    total_crackers = darren_total + calvin_total

    result = total_crackers
    return result

print(solution())