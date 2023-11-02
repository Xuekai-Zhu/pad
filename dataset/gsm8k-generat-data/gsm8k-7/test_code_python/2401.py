def solution():
    escape_time = 3  # in hours
    initial_speed = 25  # in mph
    search_time = 2  # in hours
    second_speed = 10  # in mph
    chase_time = 0.5  # in hours
    chasing_speed = 50  # in mph

    # Calculate the distance the tiger traveled before slowing down
    initial_distance = initial_speed * escape_time
    search_distance = second_speed * search_time
    total_distance = initial_distance + search_distance

    # Calculate the distance the tiger traveled while being chased
    chasing_distance = chasing_speed * chase_time

    # Calculate the total distance from the zoo where the tiger was caught
    total_distance += chasing_distance
    result = total_distance
    return result

print(solution())