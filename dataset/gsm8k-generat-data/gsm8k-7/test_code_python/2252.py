def solution():
    mary_speed = 5  # miles per hour
    jimmy_speed = 4  # miles per hour
    time = 1  # hour

    # Calculate the total distance covered by Mary and Jimmy after 1 hour
    mary_distance = mary_speed * time
    jimmy_distance = jimmy_speed * time

    # Calculate the total distance between Mary and Jimmy after 1 hour
    total_distance = mary_distance + jimmy_distance
    result = total_distance
    return result

print(solution())