def solution():
    num_flights = 20
    time_per_flight = 11  # seconds
    bomb_timer = 72  # seconds
    time_spent_running = 165  # seconds

    # Calculate the total time Ned needs to reach the top floor
    total_time_running = num_flights * time_per_flight

    # Calculate the time Ned will have to diffuse the bomb
    time_to_diffuse = bomb_timer - (time_spent_running + total_time_running)
    result = time_to_diffuse
    return result

print(solution())