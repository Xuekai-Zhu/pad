def solution():
    distance = 180  # miles
    time = 4  # hours
    speed = distance / time  # miles per hour

    additional_time = 3  # hours
    additional_distance = speed * additional_time
    result = additional_distance
    return result

print(solution())