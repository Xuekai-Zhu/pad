def solution():
    pickup_time = 6 * 60  # convert to minutes
    travel_time = 40
    arrival_time = 9 * 60  # convert to minutes

    # Calculate the total travel time
    total_time = arrival_time - (pickup_time + travel_time)
    result = total_time
    return result

print(solution())