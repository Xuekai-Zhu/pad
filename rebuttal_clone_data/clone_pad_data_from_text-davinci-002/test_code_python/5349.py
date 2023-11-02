def solution():
    distances = [50, 80]
    times = [3, 4]
    total_distance = 0
    for i in range(len(distances)):
        total_distance += distances[i] * times[i]
    result = total_distance
    return result

print(solution())