def solution():
    initial_distance = 2000
    percent_increase = 40
    increased_distance = initial_distance * (percent_increase / 100)
    total_distance = initial_distance + increased_distance
    result = total_distance / 2
    return result

print(solution())