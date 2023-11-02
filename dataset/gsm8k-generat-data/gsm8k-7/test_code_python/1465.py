def solution():
    up_flights = 3
    down_flights = 6
    steps_per_flight = 12
    step_height = 8 / 12  # convert inches to feet

    # Calculate the total distance Jack goes up
    up_distance = up_flights * steps_per_flight * step_height

    # Calculate the total distance Jack goes down
    down_distance = down_flights * steps_per_flight * step_height

    # Calculate the difference in distance
    total_distance = down_distance - up_distance
    result = total_distance
    return result

print(solution())