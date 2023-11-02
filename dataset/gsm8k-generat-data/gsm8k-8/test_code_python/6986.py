def solution():
    # Define the distance to and from the event
    distance_to_event = 200
    distance_from_event = 200

    # Calculate the total distance traveled
    total_distance = distance_to_event + distance_from_event

    # Calculate the total cost of cab rides
    cab_cost_per_mile = 2.5
    total_cost = total_distance * cab_cost_per_mile

    result = total_cost
    return result

print(solution())