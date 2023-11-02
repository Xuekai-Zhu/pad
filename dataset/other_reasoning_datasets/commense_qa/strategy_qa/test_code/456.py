def solution():
    longest_swim_distance = 139.8
    distance_from_nyc_to_miami = 1000
    if longest_swim_distance < distance_from_nyc_to_miami:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())