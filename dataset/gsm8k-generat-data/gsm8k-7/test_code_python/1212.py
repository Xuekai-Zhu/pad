def solution():
    darren_boxes = 4
    crackers_per_box = 24

    calvin_boxes = 2 * darren_boxes - 1

    # Calculate the total number of crackers bought by Darren
    darren_crackers = darren_boxes * crackers_per_box

    # Calculate the total number of crackers bought by Calvin
    calvin_crackers = calvin_boxes * crackers_per_box

    # Calculate the total number of crackers bought altogether
    total_crackers = darren_crackers + calvin_crackers
    result = total_crackers
    return result

print(solution())