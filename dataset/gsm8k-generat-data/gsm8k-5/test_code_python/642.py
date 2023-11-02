def solution():
    total_distance = 10 + 15 + 5  # Tony needs to drive a total of 30 miles for his errands
    halfway_distance = total_distance / 2  # Tony needs to drive halfway through his errands

    # Keep track of the distance Tony has driven so far
    distance_driven = 0
    if halfway_distance <= 10:
        distance_driven = halfway_distance  # Tony only needs to drive to get groceries
    elif halfway_distance <= 25:
        distance_driven = 10 + (halfway_distance - 10) * 2 / 3  # Tony needs to get groceries and a haircut
    else:
        distance_driven = total_distance - (halfway_distance - 25)  # Tony needs to get everything done

    result = distance_driven
    return result

print(solution())