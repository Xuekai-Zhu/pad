def solution():
    # Calculate the total time spent driving without rest stops
    total_driving_time = 600 / 50

    # Calculate the number of rest stops taken
    num_rest_stops = (total_driving_time // 2) - 1

    # Calculate the total time spent making rest stops
    total_rest_time = num_rest_stops * 15 + 10

    # Calculate the total time for the trip
    total_time = total_driving_time + total_rest_time

    # Calculate the number of gallons of gas used
    gas_used = 600 / 18

    # Check if a refill is needed
    if gas_used >= 15:
        total_time += 10

    # Return the total time in minutes
    result = total_time * 60
    return result

print(solution())