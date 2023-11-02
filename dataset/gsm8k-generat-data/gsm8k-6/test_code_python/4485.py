def solution():
    # Calculate the total distance to the beach and the time it takes to get there
    distance_to_beach = 16 * (1/8)  # each block is 1/8th of a mile
    time_to_beach = distance_to_beach / (x/60)  # x is the speed in miles per hour, converted to minutes per mile

    # Check if Jack can make it to the beach before the ice cream melts
    if time_to_beach <= 10:
        result = x
    else:
        result = "Jack cannot make it to the beach before the ice cream melts."
    return result

print(solution())