def solution():
    total_floors = 12
    gated_floors = [i for i in range(1, total_floors+1) if i % 3 == 0]  # List of floors with gates
    gate_time = 2 * len(gated_floors)  # Total time spent at gates
    floor_distance = 800  # Distance between floors in feet
    floor_speed = 10  # Speed in feet per second
    floor_time = floor_distance / floor_speed  # Time to travel between floors in seconds
    total_travel_time = (total_floors - 1) * floor_time  # Time to travel all floors except the first

    # Add time spent at gates and time to travel from the first floor to get the total time
    total_time = gate_time + total_travel_time

    result = total_time
    return result

print(solution())