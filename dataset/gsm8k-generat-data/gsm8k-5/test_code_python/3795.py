def solution():
    # Calculate the total distance Natasha traveled
    total_distance = 60

    # Calculate the time it should have taken her to travel the total distance at the speed limit
    time_at_speed_limit = total_distance / (x - 10)  # x is the speed limit

    # Use the time and distance information to set up an equation and solve for x (the speed limit)
    x = total_distance / (1 + time_at_speed_limit)

    result = x
    return result

print(solution())