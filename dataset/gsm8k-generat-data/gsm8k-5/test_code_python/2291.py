def solution():
    distance_walked = 1  # Trish walks 1 mile on the first day
    day = 1  # It's the first day

    while distance_walked <= 10:  # Keep iterating until Trish walks more than 10 times the distance on the first day
        distance_walked *= 2  # Double the distance walked each day
        day += 1  # Increment the day counter

    result = day
    return result

print(solution())