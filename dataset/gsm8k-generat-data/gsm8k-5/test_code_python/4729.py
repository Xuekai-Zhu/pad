def solution():
    swing_speed = 10  # The monkey can swing at a speed of 10 feet per second
    run_speed = 15  # The monkey runs at a speed of 15 feet per second when frightened
    time_running = 5  # The monkey runs for 5 seconds to evade the predator
    time_swinging = 10  # The monkey swings for 10 seconds to add distance between itself and the predator

    # Calculate the distance the monkey runs
    distance_running = run_speed * time_running

    # Calculate the distance the monkey swings
    distance_swinging = swing_speed * time_swinging

    # Calculate the total distance the monkey travels
    total_distance = distance_running + distance_swinging
    result = total_distance
    return result

print(solution())