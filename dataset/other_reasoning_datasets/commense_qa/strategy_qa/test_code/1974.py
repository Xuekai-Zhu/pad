def solution():
    max_distance = 15000
    distance_bucharest_nyc = 7670
    if distance_bucharest_nyc <= max_distance:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())