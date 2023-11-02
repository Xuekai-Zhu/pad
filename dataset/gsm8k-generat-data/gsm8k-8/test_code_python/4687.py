def solution():
    # Define the time Delaney left his home
    delaney_left = 7.5

    # Define the time he needed to reach the pick-up point
    time_to_reach = 0.5

    # Define the time the bus leaves
    bus_leaves = 8.0

    # Calculate the time difference
    time_diff = bus_leaves - (delaney_left + time_to_reach)

    # Convert the time difference to minutes
    time_diff = time_diff * 60

    result = time_diff
    return result

print(solution())