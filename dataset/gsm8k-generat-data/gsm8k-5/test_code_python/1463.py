def solution():
    num_of_flights = 20  # The building has 20 flights of stairs
    time_per_flight = 11  # Ned can run up one flight of stairs in 11 seconds

    # Calculate the total time Ned spent running up the stairs
    total_time_running_stairs = num_of_flights * time_per_flight

    time_left_for_diffusing_bomb = 72 - (total_time_running_stairs - 165)  # 165 seconds spent running up stairs

    result = time_left_for_diffusing_bomb
    return result

print(solution())