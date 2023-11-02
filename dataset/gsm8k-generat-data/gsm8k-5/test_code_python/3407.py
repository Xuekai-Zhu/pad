def solution():
    andrew_distance = 2
    peter_distance = andrew_distance + 3
    days = 5

    # Calculate the total distance both Peter and Andrew have run in 5 days
    total_distance = (andrew_distance + peter_distance) * days
    result = total_distance
    return result

print(solution())