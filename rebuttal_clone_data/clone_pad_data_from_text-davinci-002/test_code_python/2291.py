def solution():
    day = 1
    walk_distance = 1
    while walk_distance <= 10:
        day = day + 1
        walk_distance = 2 * walk_distance
    result = day
    return result

print(solution())