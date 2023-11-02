def solution():
    # Calculate the total distance Tony needs to drive
    total_distance = 10 + 15 + 5

    # Calculate half of the total distance
    half_distance = total_distance / 2

    # Keep track of the distance driven so far
    distance_driven = 0

    # Keep track of the number of errands completed
    errands_completed = 0

    # Drive to get groceries
    distance_driven += 10
    errands_completed += 1

    # Check if Tony has driven halfway through his errands
    if distance_driven >= half_distance:
        return distance_driven

    # Drive to get a haircut
    distance_driven += 15
    errands_completed += 1

    # Check if Tony has driven halfway through his errands
    if distance_driven >= half_distance:
        return distance_driven

    # Drive to go to a doctor's appointment
    distance_driven += 5
    errands_completed += 1

    # Check if Tony has driven halfway through his errands
    if distance_driven >= half_distance:
        return distance_driven

    # If Tony has not driven halfway through his errands, return the total distance
    return total_distance

print(solution())