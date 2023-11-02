def solution():
    distance = 360  # in miles
    time = 3  # in hours

    # Calculate the speed of the train
    speed = distance / time

    # Calculate the additional time required to travel 240 miles
    additional_distance = 240
    additional_time = additional_distance / speed
    result = additional_time
    return result

print(solution())