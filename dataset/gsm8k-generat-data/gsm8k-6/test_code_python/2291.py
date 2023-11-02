def solution():
    distance_walked = 1 # distance walked on the first day
    day_counter = 1 # keep track of the number of days

    while distance_walked <= 10:
        distance_walked *= 2 # double the distance walked each day
        day_counter += 1

    result = day_counter
    return result

print(solution())